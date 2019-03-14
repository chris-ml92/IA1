""" 
Python program to solve the N Queen Problem in different ways:

	Constraint Propagation and Backtracking
	Local optimization (hill climbing)
	Global optimization (simulated annealing)
	Global optimization (genetic)

Change global var N to change the problem size.
Change global var K to change how many iterations per solver.
Change global var division for text separation layout.
"""
import sys
import copy

global N 
N = 8
global K
K = 100
global division
division = '\n'+'-'*75+'\n'

# Same starting conditions for all the solvers inside problem_set
def run_all(problem_set):

	print('Backtracking (depth-first search):\n')
	printSolution( csp_back(N), N )
	
	print(division)

	print('Problem to be solved:\n')
	printSolution(single_problem, N)
	print(division)

	print('First choice hill climb:\n')
	printSolution( first_choice_hill_climb(single_problem, N, 10), N )
	
	print(division)

	print('Steepest ascent hill climb:\n')
	printSolution( steepest_ascent_hill_climb(single_problem, N), N )
	
	print(division)

	print('Random restart hill climb:\n')
	printSolution( random_restart_hill_climb(single_problem, N), N )
	
	print(division)

	print('Simulated annealing:\n')
	printSolution( simulated_annealing(single_problem, N), N )

	print(division)

	print('Genetic solver:\n')
	printSolution( genetic_solver(single_problem, N), N )

# --- Main Program ---
print('PROGRAM STARTED')
print(division)

from solvers import *

# Generate an array of problems to be solved and analyzed
single_problem = gen_problem(N)
#problem_set = [gen_problem() for _ in range(K)]

# Run the solvers
run_all(single_problem)
#run_all(problem_set)

print(division)
print('PROGRAM ENDED')