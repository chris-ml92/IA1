import backtracking, genetic_lib, hill_lib

global division
division = '\n'+'-'*75+'\n'

if __name__ == "__main__":
	print('PROGRAM STARTED')
	print(division)
	# Board Size
	N = 8
	# Max Steps
	S = 10000
	# Restarts
	R = 10
	# Backtracking
	print('Backtracking (depth-first search):\n')
	solution_b = backtracking.csp_back(N)
	backtracking.printSolution(solution_b, N)
	print(division)

	print('Problem to be solved:\n')
	problem = backtracking.gen_problem(N)
	backtracking.printSolution(problem, N)
	print(division)

	print('Hill climb:\n')
	solution_h, steps = hill_lib.hill_climb(problem, S, N)
	backtracking.printSolution(solution_h, N)
	print(division)

	print('Hill climb with restarts:\n')
	best_sol = None
	best_sol_steps = S+1
	for run in range(R):
		sol, steps = hill_lib.hill_climb(problem, S, N)
		if steps < best_sol_steps:
			best_sol = sol
			best_sol_steps = steps
			print("Best solution so far:"+str(best_sol_steps) ) 

	print("Best solution found steps value: "+str(best_sol_steps)+"\n" ) 
	backtracking.printSolution(best_sol, N)
	print(division)
	
	print('Genetic:\n')
	solution_g = genetic_lib.genetic(problem, S, N)
	backtracking.printSolution(solution_g, N)
	print(division)
	
	print('PROGRAM ENDED')
