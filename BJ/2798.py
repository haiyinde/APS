from itertools import combinations as cb

N, M = map(int, input().split())
cards = list(map(int, input().split()))
biggest_num = 0

for c in cb(cards, 3):
    temp_sum = sum(c)
    if biggest_num < temp_sum <= M:
        biggest_num = temp_sum

print(biggest_num)
