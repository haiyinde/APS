# type annotation 잊지말기,, 자꾸 까먹
N, M = map(int, input().split())
A: set = set(map(int, input().split()))
B: set = set(map(int, input().split()))

print(len(A-B)+len(B-A))