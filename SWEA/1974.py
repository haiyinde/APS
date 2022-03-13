# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for r in sudoku:
        if sum(r) != 45:
            result = 0
            break

    for r in zip(*sudoku):
        if sum(r) != 45:
            result = 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = 0
            for k in range(3):
                for l in range(3):
                    tmp += sudoku[i+k][j+l]
            if tmp != 45:
                result = 0
                break
                # tmp += sudoku[i][j] + sudoku[i+1][j] + sudoku[i+2][j] \
                #        + sudoku[i+1][j] + sudoku[i+1][j+1] + sudoku[i][j+2] \
                #        + sudoku[i+2][j] + sudoku[i+2][j+1] + sudoku[i+2][j+2]

    print("#{} {}".format(t, result))

