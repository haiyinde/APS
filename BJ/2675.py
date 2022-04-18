T = int(input())
for t in range(T):
    R, S = input().split()
    R = int(R)
    for s in S:
        print(s*R, end='')
    print()