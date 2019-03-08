import random, sys


def printBoard(sol):
    board = []
    for i in range(nQueens):
        board.append([])
        for j in range(nQueens):
            board[i].append(0)

    for i in range(nQueens):
        board[sol[i]][i] = 1

    for i in range(nQueens):
        for j in range(nQueens):
            print(board[i][j], " ", end=' ')
        print()


def random_pos(Conflictlist, condition):
        x = random.choice([i for i in range(nQueens) if condition(Conflictlist[i])])
        return x

def min_conflict_value(sol, csp, var):
    n_conflicts_col = []
    for row in range(csp):
        n_conflicts_col.append(find_conflictss(sol,csp,var,row))
    return n_conflicts_col

def min_conflicts(sol, csp, max_steps=1000):

    #for i = 1 to max steps do
    #if current is a solution for csp then return current
    #var ←a randomly chosen conflicted variable from csp.V ARIABLES
    #value ← the value v for var that minimizes CONFLICTS (var,v,current,csp)
    #set var =value in current
    #return failure
    
    couter = 0
    for i in range(max_steps):
        
        number_conflicts = All_conflicts(sol, csp)
        
        if sum(number_conflicts) == 0:
            print("Solved in " + str(couter) + " steps\nThe solution found is: " +str(sol) +"\n")
            return sol
        
        var = random_pos(number_conflicts, lambda x: x > 0)
        listConflictsCol = min_conflict_value(sol,csp,var)
        sol[var] = random_pos(listConflictsCol, lambda x: x == min(listConflictsCol))
        couter += 1
        
    raise Exception("Incomplete solution: try more iterations.")

def All_conflicts(sol, csp):
    return [find_conflictss(sol, csp, var, sol[var]) for var in range(csp)]

def find_conflictss(sol, csp, var, row):
    total = 0
    for i in range(csp):
        if i == var:
            continue
        if sol[i] == row or abs(i - var) == abs(sol[i] - row):
            total += 1
    return total

if __name__ == "__main__":

    nQueens = 100
    sol = min_conflicts(list(range(nQueens)),nQueens)
    printBoard(sol)