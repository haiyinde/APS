sugar = int(input())
sack = 0
while sugar >= 0:
    if sugar % 5 == 0:
        sack += sugar//5
        print(sack)
        break
    sugar -= 3
    sack += 1
else:
    print(-1)