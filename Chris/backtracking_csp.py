import random


class Queen:
    def __init__(self, N):
        self.diagonals = {}
        self.anti_diagonals = {}
        self.rows = {}
        self.columns = {}
        self.N = N
        self.board = [[0 for x in range(N)] for y in range(N)]

def is_cell_safe(Queen, r, c):
    if r in Queen.rows:
        return False
    if c in Queen.columns:
        return False
    if r - c in Queen.diagonals:
        return False
    if r + c  in Queen.anti_diagonals:
        return False

    return True

def place_a_queen(Queen, r, c):
    Queen.rows[r] = True
    Queen.columns[c] = True
    Queen.diagonals[r - c] = True
    Queen.anti_diagonals[r + c] = True
    Queen.board[r][c] = 1

def undo_placing_a_queen(Queen, r, c):
    del Queen.rows[r]
    del Queen.columns[c]
    del Queen.diagonals[r - c]
    del Queen.anti_diagonals[r + c]
    Queen.board[r][c] = 0

def solve(Queen, column):
    if column == Queen.N:
       return True
    for i in range(0,Queen.N):
        if is_cell_safe(Queen,i, column):
           place_a_queen(Queen,i, column)
           if solve(Queen , column + 1) == True:
              return True
           undo_placing_a_queen(Queen,i, column)
    return False


if __name__ == "__main__":

    sol = Queen(8)
    col = random.randint(0,7)
    place_a_queen(sol,col,0)
    solve(sol,1)