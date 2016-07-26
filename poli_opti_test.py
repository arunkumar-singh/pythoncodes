# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:08:10 2016

@author: aks
"""

import numpy as np
import cvxopt
import mompy as mp

# just some basic settings and setup
mp.cvxsolvers.options['show_progress'] = False
from IPython.display import display, Markdown, Math, display_markdown

sp.init_printing()

#def print_problem(obj, constraints = None, moment_constraints = None):
    #display_markdown(mp.problem_to_str(obj,constraints,moment_constraints, False), raw=True)

x,y = sp.symbols('x,y')
f =  x**2 + y**2
gs = [x+y>=4, x+y<=4]
#print_problem(f, gs)
sol = mp.solvers.solve_GMP(f, gs)
mp.extractors.extract_solutions_lasserre(sol['MM'], sol['x'], 1)    



