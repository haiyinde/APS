from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
keys = list(map(int, input().split()))

count_list = Counter(cards)
for key in keys:
    print(count_list[key])