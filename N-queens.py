def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1:return False
    return True
def solve_n_queens(n):
    solutions = []
    def backtrack(row, board):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1, board)
                board[row][col] = 0
    backtrack(0, [[0] * n for _ in range(n)])
    return solutions
def print_solutions(solutions):
    if solutions:
        for sol in solutions:
            for row in sol:
                print(''.join(map(str, row)))
            print()
    else:
        print("Not Possible!")
N = int(input("Enter the number of Queens: "))
print_solutions(solve_n_queens(N))


"""python N-queens.py
Enter the number of Queens: 4
0100
0001
1000
0010

0010
1000
0001
0100
"""