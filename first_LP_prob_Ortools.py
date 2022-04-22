# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:29:28 2022

@author: Shweta
"""

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GlOP')

x = solver.NumVar(45,1000,'x')

y = solver.NumVar(5,1000,'y')

solver.Add(50*x+24*y<=2400)

solver.Add(30*x+33*y<=2100)



solver.Maximize(x+y-50)

results = solver.Solve()

if results == pywraplp.Solver.OPTIMAL: print('Optimal Found')

print('x:', x.solution_value())
print('y:', y.solution_value())



