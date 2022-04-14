A, B, C = map(int, input().split())

if A == B and B == C and C == A:
    print(10000+A*1000)
elif A != B and B != C and C != A:
    M = max(A, B, C)
    print(M*100)
elif A == B or B == C:
    print(1000+B*100)
elif A == C:
    print(1000+A*100)
