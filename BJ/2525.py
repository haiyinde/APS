A, B = map(int, input().split())
C = int(input())

X = A*60+B+C
H = (X//60)%24
M = X%60

print(H, M)