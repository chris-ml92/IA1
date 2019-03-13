import backtracking, optimized_backtracking, genetic_lib, hill_lib
from timeit import default_timer as timer

global division
division = '\n'+'-'*75+'\n'

if __name__ == "__main__":
	print('PROGRAM STARTED')
	print(division)
	
	# Board Size
	N = 24
	
	# Max Steps
	S = 10000
	
	# Restarts
	R = 10
	
	# Backtracking
	print('Backtracking (depth-first search):\n')
	start_time = timer()
	backtracking.csp_back(N)
	print("Completed in "+str(round((timer()-start_time), 3))+" seconds.\n" )
	print(division)
	
	# Backtracking Optimized
	print('Optimized Backtracking (depth-first search):\n')
	start_time = timer()
	optimized_backtracking.optimized_csp_back(N)
	print("Completed in "+str(round((timer()-start_time), 3))+" seconds.\n" )
	print(division)
	
	# The problem for Hill Climbing
	print('Problem to be solved:\n')
	problem = backtracking.gen_problem(N)
	backtracking.printSolution(problem, N)
	print(division)
	
	# Hill without restarts
	print('Hill climb:\n')
	start_time = timer()
	solution_h, steps = hill_lib.hill_climb(problem, S, N)
	print("Completed in "+str(round((timer()-start_time), 3))+" seconds.\n" )
	backtracking.printSolution(solution_h, N)
	print(division)
	
	# Hill with restarts
	print('Hill climb with restarts:\n')
	start_time = timer()
	best_sol = None
	best_sol_steps = S+1
	for run in range(R):
		sol, steps = hill_lib.hill_climb(problem, S, N)
		if steps < best_sol_steps:
			best_sol = sol
			best_sol_steps = steps
			print("Best solution so far:"+str(best_sol_steps) ) 

	print("Best solution found steps value: "+str(best_sol_steps)+"\n" ) 
	print("Completed in "+str(round((timer()-start_time), 3))+" seconds.\n" )
	backtracking.printSolution(best_sol, N)
	print(division)

	# Genetic 	
	print('Genetic:\n')
	start_time = timer()
	solution_g = genetic_lib.genetic(problem, S, N)
	print("Completed in "+str(round((timer()-start_time), 3))+" seconds.\n" )
	backtracking.printSolution(solution_g, N)
	print(division)
	
	print('PROGRAM ENDED')
