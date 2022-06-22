import sys

K: int = int(input())
numbers: list = list(int(sys.stdin.readline().rstrip()) for _ in range(K))
result: list = list()

for num in numbers:
    if num == 0:
        result.pop(-1)
    else:
        result.append(num)

print(sum(result))