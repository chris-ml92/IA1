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
def mutate(a, mutation_prob):
	if random.random() < mutation_prob:
		n = len(a)
		x = random.randint(0, n - 1)
		y = random.randint(0, n - 1)
		a[x] = y

	return a

def Selection(population, probabilities, start,end):
	populationWithProbabilty = [(a,b) for a,b in zip(population, probabilities)]
	best = None
	best_p = -1

	for i in range(start,end+1):
		pop,prob = populationWithProbabilty[i]
		if prob > best_p:
			best_p = prob
			best = pop

	return best

# Generate a new population using best mother and fathers
def new_gen_population(population, max_pop, pList, mutation_prob, N, prob_crossover):
	# Populations
	new_pop_list = []
	list_of_leaders = []
	
	for i in range(0, max_pop, N):
		list_of_leaders.append(Selection(population, pList, i, i+N-1 ))
	
	# Generate new pop using list_of_leaders
	for i in range(0, int(max_pop/2)):
		mother = random.choice(list_of_leaders)
		father = random.choice(list_of_leaders)

		# If we find two identical ndividuals we just mutate one of them
		# Increase mutations in late runs.
		# TO BE OPTIMIZED 
		if mother == father and mutation_prob < 1:
			mutation_prob += 0.05

		childL = crossover(mother, father, N, prob_crossover)

		child1 = mutate(childL[0], mutation_prob)
		child2 = mutate(childL[1], mutation_prob)

		new_pop_list.append(child1)
		new_pop_list.append(child2)

	return new_pop_list

def random_individual(N):
	list = []
	for i in range(N):
		list.append(random.randint(0, N-1))
	return list

def probs(n , fitness, max_fitness, sumFitnesses):
	return fitness(n, max_fitness)/sumFitnesses

def genetic(problem, max_generations, N):
	max_population = (N**2)*2
	prob_crossover = 0.9
	prob_mutation = 0.15
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

	# Init stop cnditions
	best_pop = None
	best_pop_fit = 0

	# While not fitness > max_fitness or max generation reached ...
	# ... continue to mix and match
	while best_pop_fit != max_fitness:
		sumFitnesses = sum([fitness(n,max_fitness) for n in population])
		pList = [probs(n, fitness, max_fitness, sumFitnesses) for n in population]
		population = new_gen_population(population, max_population, pList, prob_mutation, N, prob_crossover)
		generation += 1
		
		# Check best so far
		for i in population:
			fit = fitness(i, max_fitness)
			if fit == max_fitness:
				print("\n\nFound solution:" + str(i) + " at generation: " + str(generation) + "\n")
				return printBoard(i, N)
			else:
				if fit > best_pop_fit:
					best_pop_fit = fit
					best_pop = i

		print("\rRunning with generation: "+str(generation)+" Fitness: "+str(best_pop_fit)+"/"+str(max_fitness)+" ", end='', flush=True )
		if generation == max_generations: break
	
	print("\nError - Solution NOT found at generation: " +str(generation) +"\n")
	print("\nBest failure returned with fit: " +str(best_pop_fit) +"\n")
	return printBoard(best_pop, N)
