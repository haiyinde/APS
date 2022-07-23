from bisect import bisect

n = int(input())
a: list = list(map(int, input().split()))
m = int(input())
b: list = list(map(int, input().split()))

a.sort()

for key in b:
    i = bisect(a, key)
    print(i)
    answer = 1 if a[i-1] == key else 0
    print(answer)

