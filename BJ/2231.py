N = int(input())
result = 0

for M in range(1, N+1):
    prtsum = list(map(int, str(M)))
    result = M + sum(prtsum)
    if result == N:
        print(M)
        break

    if M == N:
        print(0)
        break
