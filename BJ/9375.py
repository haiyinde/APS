from collections import defaultdict

T = int(input())
for tc in range(T):
    n = int(input())
    clothes = defaultdict(list)
    for _ in range(n):
        name, type = input().split()
        clothes[type].append(name)

    result = 1
    for value in clothes.values():
        result *= len(value)+1

    print(result-1)
