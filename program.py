""" 
Python program to solve N QUeen Problem in different ways:

    Constraint Propagation and Backtracking
    Local optimization (hill climbing)
    Global optimization (simulated annealing)

Change global var N to change the problem size.
Change global var K to change how many iterations per solver.
Change global var division for text separation layout.
"""
global N = 8
global K = 100
global division = '\n'+'-'*75+'\n'

# Same starting conditions for all the solvers inside problem_set
# We can compare solver results
def run_all(problem_set):

    print('CSP And backtracking:\n')
    run_one(problem_set, first_choice_hill_climb)
    
    print(division)

    print('First choice hill climb:\n')
    run_one(problem_set, first_choice_hill_climb)
    
    print(division)

    print('Steepest ascent hill climb:\n')
    run_one(problem_set, steepest_ascent_hill_climb)
    
    print(division)

    print('Random restart hill climb:\n')
    run_one(problem_set, lambda x: random_restart_hill_climb(problem_set[0].__class__))
    
    print(division)

    print('Simulated annealing:\n')
    run_one(problem_set, lambda x: simulated_annealing(x, [0.9**(0.05*i-10) for i in range(1, 2000)]))

# Solver execution wrapper
def run_one(problem_set, search_function):

    num_iterations = len(problem_set)

    results = []
    for problem_num, problem in enumerate(problem_set):
        print('\rSolving problem ' + str(problem_num+1) + ' of ' + str(num_iterations), end='', flush=True)
        start_time = timer()
        result = search_function(problem)
        result['time'] = (timer()-start_time)*1000
        result['optimal_cost'] = problem.optimal_solution_cost()
        result['path_length'] = len(result['solution'])-1
        results.append(result)

    print(' '*50 + '\r', end='', flush=True)

    # Aggregate results
    results = [results,
               [result for result in results if result['outcome'] == 'success'],
               [result for result in results if result['outcome'] == 'failure']]

    print_results(results)

# Main
print(' --- PROGRAM STARTED --- \n')
print(division)

from queens import QueensProblem

# Generate an array of problems to be solved and analyzed
problem_set = [QueensProblem() for _ in range(K)]

# Run the solvers
run_all(problem_set)

print(division)
print(' --- PROGRAM ENDED --- \n')