import sympy as sp
import sys

# import custom modules
import f_functionclass as ff
import f_compare as fc
import f_aux as fa
import f_define as fd
import f_random as fr
import f_plots as fpl

# import p_problem as pp

# import j_problem as jpr
# 
# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = \
    sp.symbols('a b c d p q r s t w x y z', real=True)

# MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
#             's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}



# f = fd.define_function(func.sym_form)


print(sys.argv[1])
