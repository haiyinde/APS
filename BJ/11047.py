import sys

N, K = map(int, input().split())
values = list(int(sys.stdin.readline()) for _ in range(N))
ascending_values: list = sorted(values, reverse=True)

coins: int = 0
i: int = 0
while K > 0:
    if K - ascending_values[i] >= 0:
        current_coins: int = K // ascending_values[i]
        K -= current_coins*ascending_values[i]
        coins += current_coins
    i += 1

print(coins)


