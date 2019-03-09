import random



def printBoard(sol):
    board = []
    for i in range(checkboard_size):
        board.append([])
        for j in range(checkboard_size):
            board[i].append(0)
    for i in range(checkboard_size):
        board[sol[i]][i] = 1

    for i in range(checkboard_size):
        for j in range(checkboard_size):
            print(board[i][j], " ", end=' ')
        print()



def calculate_max_fitness():
    max = int((checkboard_size * (checkboard_size - 1)) * 0.5)
    return max



def random_individual(checkboard_size):
    list = []
    for i in range(checkboard_size):
        list.append(random.randint(0, checkboard_size - 1))
    return list



def fitness(queens):
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



def crossover(a,b):
    lists = []
    child1 = []
    child2 = []

    if random.random() < prob_crossover:
        #crossPoint = int(checkboard_size/2)
        p1 = random.randint(3,checkboard_size-1)

        for i in range(p1):
            child1.append(a[i])
            child2.append(b[i])
        for i in range(p1,checkboard_size):
            child1.append(b[i])
            child2.append(a[i])
        lists.append(child1)
        lists.append(child2)
        return lists
    else:
        lists.append(a)
        lists.append(b)
        return lists



def mutate(a,mutation_prob):
    if random.random() < mutation_prob:
        n = len(a)
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        a[x] = y

    return a


def randomSelection(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

def parents(population,max_pop, rel_pop, mutation_prob):
    newPop = []
    for i in range(0, int(max_pop/2)):
        #mother = random.randint(0, rel_pop)
        #father = random.randint(0, rel_pop)
        #check parents are not the same
        #while mother == father:
         #   father = random.randint(0,rel_pop)
        mother = randomSelection(population, rel_pop)
        father = randomSelection(population, rel_pop)

        childL = crossover(mother, father)

        child1 = mutate(childL[0], mutation_prob)
        child2 = mutate(childL[1], mutation_prob)
        newPop.append(child1)
        newPop.append(child2)

    return newPop


def probs(n , fitness):
    return fitness(n)/max_fitness

def genetic(population, fitness):

    #population = sorted(population, key=lambda x: fitness(x), reverse=True)
    #relevant_population = int(max_population/2)
    pList = [probs(n,fitness) for n in population]
    new_pop = parents(population, max_population, pList, prob_mutation)
    #new_pop = sorted(new_pop, key=lambda x: fitness(x), reverse=True)
    return new_pop



def genetic(problem, N):
    checkboard_size = N
    max_population = 500
    prob_crossover = 0.8
    prob_mutation = 0.05
    max_fitness = calculate_max_fitness()
    population = []
    generation = 0

    for i in range(max_population):
        population.append(random_individual(checkboard_size))

    while not max_fitness in [fitness(i) for i in population]:
        population = genetic(population, fitness)
        generation += 1
        print("generation:" + str(generation) + "\n" )
        if generation == 100000: break

    stop = 0
    for i in population:
        if stop == 1:break
        if fitness(i) == max_fitness:
            print("Found solution:" + str(i) + " at generation: " + str(generation) + "\n")
            printBoard(i)
            stop = 1