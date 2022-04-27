T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    flat = [i for i in range(1, n + 1)]
    for __ in range(k):
        for j in range(1, n):
            flat[j] += flat[j-1]

    print(flat[-1])

