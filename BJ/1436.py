N = int(input())
dooms_number = 666
while N != 0:
    if "666" in str(dooms_number):
        N -= 1
        if N == 0:
            break
    dooms_number += 1
print(dooms_number)