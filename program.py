""" 
Python program to solve N QUeen Problem in different ways:

    Constraint Propagation and Backtracking
    Local optimization (hill climbing)
    Global optimization (simulated annealing)
    Global optimization (genetic)

Change global var N to change the problem size.
Change global var K to change how many iterations per solver.
Change global var division for text separation layout.
"""
global N 
N = 8
global K
K = 100
global division
division = '\n'+'-'*75+'\n'

# --- Auxiliary Functions ---

# Print solutions
def printSolution(board): 
	for i in range(N): 
		for j in range(N): 
			print board[i][j], 
		print

# Same starting conditions for all the solvers inside problem_set
def run_all(problem_set):

    print('Backtracking (depth-first search):\n')
    printSolution( csp_back(N) )
    
    print(division)

    print('First choice hill climb:\n')
    printSolution( first_choice_hill_climb(single_problem) )
    
    print(division)

    print('Steepest ascent hill climb:\n')
    printSolution( steepest_ascent_hill_climb(single_problem) )
    
    print(division)

    print('Random restart hill climb:\n')
    printSolution( random_restart_hill_climb(single_problem) )
    
    print(division)

    print('Simulated annealing:\n')
    printSolution( simulated_annealing(single_problem) )

    print(division)

    print('Simulated annealing:\n')
    printSolution( genetic_solver(single_problem) )

# Generate boards with random placed queens
def gen_problem():
    board = [[0 for x in range(N)] for y in range(N)]

    from random import randint

    for _ in range(N):
        board[randint(0, N-1)][randint(0, N-1)] = 1    
    return board

# --- Main Program ---
print(' --- PROGRAM STARTED --- ')
print(division)

from solvers import *

# Generate an array of problems to be solved and analyzed
single_problem = gen_problem()
#problem_set = [gen_problem() for _ in range(K)]

# Run the solvers
run_all(single_problem)
#run_all(problem_set)

print(division)
print(' --- PROGRAM ENDED --- ')