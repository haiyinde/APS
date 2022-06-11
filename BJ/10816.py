N = int(input())
cards = list(map(int, input().split()))
cards_dict = dict()
M = int(input())
criterias = list(map(int, input().split()))

for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

for c in criterias:
    print(cards_dict.get(c, 0), end=" ")
