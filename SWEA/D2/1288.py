#D2
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = input()
    counted = [False] * 9
    result = 0

    while not counted == [True]*9:
        numbers = list(map(int, list(N)))
        result += 1
        for n in numbers:
            if counted[n] == False:
                counted[n] = True
        N = str(int(N)*2)


    print("#{} {}".format(t, result))