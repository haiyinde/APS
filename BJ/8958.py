for _ in range(int(input())):
    results = list(input())
    count = 0
    total = 0
    for r in results:
        if r == "O":
            count += 1
            total += count
        else:
            count = 0
    print(total)
