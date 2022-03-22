#D2
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    counted = [False] * 10
    i = 0

    while False in counted:
        i += 1
        numbers = str(N*i)
        for num in numbers:
            counted[int(num)] = True

    print("#{} {}".format(t, numbers))