import re
from math import isclose
import pymatgen.core as pg
import re
import numpy as np
from math import isclose, lcm
from ElMD import ElMD
from fractions import Fraction
from z3.z3 import RatNumRef
from comgen.query import element_to_pettifor

def composition_to_pettifor_array(comp):
    """
        Create an array representation of comp.
        Position i is normed quantity of the element with pettifor number i.
    """
    if isinstance(comp, str):
        comp = pg.Composition(comp)

    comp_array = [0.0]*103
    for el in comp.elements:
        p_num = element_to_pettifor(el)
        comp_array[p_num] = float(comp.get_atomic_fraction(el))

    return comp_array

# def elmd(comp1, comp2):
#     return np.sum(np.absolute(np.cumsum(np.array(comp1) - np.array(comp2))))

def get_target_composition_from_model(model):
    comp = {}
    for name, val in model.items():
        if val == 0: continue
        if name.endswith('_elementquantity'):
            x = re.search(r'TargetComposition[0-9]*', name)
            elt = name[x.end():]
            x = re.search(r'[A-Z][a-z]?', elt)
            elt = elt[x.start():x.end()]
            comp[elt] =  float(val)

    return pg.Composition(comp)

def get_target_composition_with_integer_quantities(comp):
    frac_comp = {el: Fraction(val) for el, val in comp.items()}
    denoms = [val.denominator for val in frac_comp.values()]
    lcm_denom = lcm(*denoms)
    for el, val in frac_comp.items():
        m = int(lcm_denom/val.denominator)
        frac_comp[el] = val.numerator*m
    int_comp = {el: int(val.numerator) for el, val in frac_comp.items()}
    return int_comp

def check_charge_balance(sq_q):
    total_charge = 0
    for sp, q in sq_q.items():
        total_charge += sp.oxi_state * q
    assert isclose(total_charge, 0)

def get_nonzero_species(model):
    def extract_charge(s):
        x = re.search(r'[0-9]?(\+|\-)', sp)
        chg = sp[x.start():x.end()]
        
        if chg == '+': chg = 1
        elif chg == '-': chg = -1
        elif '-' in chg: chg = -int(chg[:-1])
        else: chg = int(chg[:-1])        
        
        return chg

    def extract_element(s):
        x = re.search(r'[A-Z][a-z]?', s)
        el = s[x.start():x.end()]
        return el

    sp_q = {}
    for name, val in model.items():
        if val == 0: continue
        if name.endswith('_speciesquantity'):
            x = re.search(r'TargetComposition[0-9]*', name)
            sp = name[x.end():]
            el = extract_element(sp)
            chg = extract_charge(sp)
            # print(sp, el, chg, val)
            sp = pg.Species(el, chg)
            # print(sp)
            sp_q[sp] = val
    return sp_q

def check_integer_composition(model_comp, pg_comp, int_comp):
    total_atoms = sum(int_comp.values())
    for el, val in int_comp.items():
        assert isclose(val/total_atoms, pg_comp.get_atomic_fraction(el), abs_tol=0.01), f"{el} {model_comp} {pg_comp} {int_comp}"
        assert isclose(val/total_atoms, Fraction(model_comp[el]), abs_tol=0.01), f"{el} {model_comp} {pg_comp} {int_comp}"

def check_distances(new_comp, model):
    for name, val in model.items():
        # check EMD values
        if name.endswith('EMDdistance'): 
            x = re.search(r'TargetComposition[0-9]*', name)
            comp = name[x.end():]
            x = re.search(r'([A-Z][a-z]?([0-9]*\.[0-9]*)?\ ?)+', comp)
            comp = comp[x.start():x.end()]
            distance = ElMD(str(new_comp)).elmd(str(comp))
            # distance = elmd(composition_to_pettifor_array(comp), composition_to_pettifor_array(new_comp))
            assert isclose(float(val), float(distance), abs_tol=0.01), f"{comp} {new_comp} {round(float(val), 3)} {round(float(distance), 3)} {float(val)-distance}"



def get_target_composition_from_model(model):
    comp = {}
    for name, val in model.items():
        if val == 0: continue
        if name.endswith('_elementquantity'):
            x = re.search(r'TargetComposition[0-9]*', name)
            elt = name[x.end():]
            x = re.search(r'[A-Z][a-z]?', elt)
            elt = elt[x.start():x.end()]
            comp[elt] =  float(val)

    return pg.Composition(comp)

def check_synthesis(comp, ing_q):
    """Make sure ingredient compositions sum to target composition"""
    for el in comp:
        el_contributions = [ing.get_atomic_fraction(el)*val for ing, val in ing_q.items()]
        input_el = sum(el_contributions)
        # print(f'{el} {input_el} {comp.get_atomic_fraction(el)} {el_contributions}')
        assert isclose(input_el, comp.get_atomic_fraction(el), abs_tol=0.01)

def get_nonzero_ingredients(model):
    ing_q = {}
    for name, val in model.items():
        if val == 0: continue
        if name.endswith('_ingredientquantity'):
            x = re.search(r'Synthesis[0-9]*', name)
            comp = name[x.end():]
            x = re.search(r'([A-Z][a-z]?[0-9]+\.?[0-9]*\ ?)+', comp)
            comp = comp[x.start():x.end()]
            comp = pg.Composition(comp)
            ing_q[comp] = val
    # print(ing_q)
    return ing_q