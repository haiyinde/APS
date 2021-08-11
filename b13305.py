N = int(input())
length = list(map(int, input().split()))
won = list(map(int, input().split()))
cost = 0

for i in range(N-1):
    if won[i] < won[i+1]:
        won[i+1] = won[i]
    cost += won[i] * length[i]
print(cost)