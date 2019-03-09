import random, sys

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

# ???
def random_pos(Conflictlist, condition, N):
    x = random.choice([i for i in range(N) if condition(Conflictlist[i])])
    return x

# Create a list of conflicting positions
def min_conflict_value(sol, csp, var):
    n_conflicts_col = []
    for row in range(csp):
        n_conflicts_col.append(find_conflictss(sol,csp,var,row))
    return n_conflicts_col

# Hill climb solver main part
def min_conflicts(sol, csp, max_steps=1000):
    print("The problem now is: " +str(sol))
    counter = 0
    for i in range(max_steps):
        
        number_conflicts = all_conflicts(sol, csp)
        
        if sum(number_conflicts) == 0:
            print("Solved in " + str(counter) + " steps\nThe solution found is: " +str(sol) +"\n")
            return sol, counter
        
        var = random_pos(number_conflicts, lambda x: x > 0, csp)
        listConflictsCol = min_conflict_value(sol,csp,var)
        sol[var] = random_pos(listConflictsCol, lambda x: x == min(listConflictsCol), csp)
        counter += 1
    
    print("Not solved after " + str(counter) + " steps\n")
    return sol, counter

# ???
def all_conflicts(sol, csp):
    return [find_conflictss(sol, csp, var, sol[var]) for var in range(csp)]

# Self explanatory
def find_conflictss(sol, csp, var, row):
    total = 0
    for i in range(csp):
        if i == var:
            continue
        if sol[i] == row or abs(i - var) == abs(sol[i] - row):
            total += 1
    return total


# Wrapper for hill climb
def hill_climb(problem, max_steps, N):
    # Wrap the board[][] to list[queen row position]
    var = []
    for j in range(N):
        for i in range(N):
            if problem[i][j] == 1:
                var.append(i)
    
    # Solve
    sol, steps = min_conflicts(var, N, max_steps)
    return printBoard(sol, N), steps
