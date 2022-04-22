### Objective
The main objective of this repo to create mathematical models of some real life business problems and solving them in different frameworks and solvers like Ortools,SCIP, CPLEX, GLPK, Pulp and Pyomo.
#### First Prob using 'Ortools': 
A manufacturer produces two products, X and Y , with two machines, A and B.

The cost of producing each unit of X is:
- for machine A: 50 minutes,
- for machine B: 30 minutes.

The cost of producing each unit of Y is:
- for machine A: 24 minutes,
- for machine B: 33 minutes.

Working plans for a particular week are:
- 40 hours of work on machine A,
- 35 hours of work on machine B.

The week starts with:
- A stock of 30 units of X and 90 of Y ,
- A demand of 75 units of X and 95 of Y .
##### Mathematical Modelling:
Maximize (x + 30 − 75) + (y + 90 − 95)

x = units of X to be produced

y = units of Y to be produced

restricted to:

50x + 24y ≤ 40 × 60

30x + 33y ≤ 35 × 60

x ≥ 75 − 30

y ≥ 95 − 90
