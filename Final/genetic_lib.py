import random

# Return a board[][] to be printed by main.py
def printBoard(sol, N):
	board = []
	for i in range(N):
		board.append([])
		for j in range(N):
			board[i].append(0)

	for i in range(N):
		board[sol[i]][i] = 1

	return board

# Max possible fitness for the board
def calculate_max_fitness(N):
	max = int((N * (N - 1)) * 0.5)
	return max

# Fitness function as num conflicts
def fitness(queens, max_fitness):
	conflicts = 0

	for i in range(len(queens)):
		for j in range(i + 1, len(queens)):
			if i != j:
				# Horizonal check
				if queens[i] == queens[j]:
					conflicts = conflicts + 1
				# Diagonal Check
				if abs(queens[i] - queens[j]) == abs(i - j):
					conflicts = conflicts + 1

	individual_fitness = max_fitness - conflicts
	return individual_fitness

# Crossing two samples
def crossover(a, b, N, prob_crossover):
	lists = []
	child1 = []
	child2 = []

	if random.random() < prob_crossover:
		#crossPoint = int(checkboard_size/2)
		p1 = random.randint(3,N-1)

		for i in range(p1):
			child1.append(a[i])
			child2.append(b[i])
		for i in range(p1, N):
			child1.append(b[i])
			child2.append(a[i])
		lists.append(child1)
		lists.append(child2)
		return lists
	else:
		lists.append(a)
		lists.append(b)
		return lists

# Random perturbation of the samples
def mutate(a,mutation_prob):
	if random.random() < mutation_prob:
		n = len(a)
		x = random.randint(0, n - 1)
		y = random.randint(0, n - 1)
		a[x] = y

	return a

# Select mother and father from best individuals 
def Selection(population, probabilities):
	populationWithProbabilty = zip(population, probabilities)
	best_mother = None
	best_father = None
	best_mother_p = 0
	best_father_p = 0

	for pop, prob  in populationWithProbabilty:
		if prob > best_mother_p:
			best_mother_p = prob
			best_mother = pop
		if prob > best_father_p and pop != best_mother:
			best_father_p = prob
			best_father = pop
			
	return best_mother, best_father

# ???
def new_gen_population(population, max_pop, rel_pop, mutation_prob, N, prob_crossover):
	newPop = []
	for i in range(0, int(max_pop/2)):
		mother, father = Selection(population, rel_pop)

		childL = crossover(mother, father, N, prob_crossover)

		child1 = mutate(childL[0], mutation_prob)
		child2 = mutate(childL[1], mutation_prob)
		newPop.append(child1)
		newPop.append(child2)
	return newPop

def random_individual(N):
	list = []
	for i in range(N):
		list.append(random.randint(0, N - 1))
	return list

def probs(n , fitness, max_fitness):
	return fitness(n, max_fitness)/max_fitness

def genetic(problem, max_generations, N):
	max_population = N*2
	prob_crossover = 0.6
	prob_mutation = 0.1
	max_fitness = calculate_max_fitness(N)
	population = []
	generation = 0
	first = []

	# Original problem provided 
	for j in range(N):
		for i in range(N):
			if problem[i][j] == 1:
				first.append(i)
	population.append(first)

	# Generate a population
	for i in range(max_population-1):
		population.append(random_individual(N))

	# While not fitness > max_fitness or max generation reached ...
	# ... continue to mix and match
	while not max_fitness in [fitness(i, max_fitness) for i in population]:
		pList = [probs(n, fitness, max_fitness) for n in population]
		population = new_gen_population(population, max_population, pList, prob_mutation, N, prob_crossover)
		generation += 1
		best_fitness = max([fitness(i, max_fitness) for i in population])
		print("\rRunning with generation: "+str(generation)+" Fitness: "+str(best_fitness)+"/"+str(max_fitness), end='', flush=True )
		if generation == max_generations: break
	
	# If the previous cycle found someting usefull use it here
	best_failure = None
	best_failure_fit = 0
	for i in population:
		fit = fitness(i, max_fitness)
		if fit == max_fitness:
			print("\nFound solution:" + str(i) + " at generation: " + str(generation) + "\n")
			return printBoard(i, N)
		else:
			if fit > best_failure_fit:
				best_failure_fit = fit
				best_failure = i
	
	print("\nError - Solution NOT found at generation: " +str(generation) +"\n")
	print("\nBest failure returned with fit: " +str(best_failure_fit) +"\n")
	return printBoard(best_failure, N)
