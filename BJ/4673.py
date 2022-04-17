def d(n):
    str_num = str(n)
    total = int(str_num)
    for i in str_num:
        total += int(i)
    return total

non_self_numbers = []
for i in range(1, 10001):
    num = d(i)
    non_self_numbers.append(num)

for j in range(1, 10001):
    if j not in non_self_numbers:
        print(j)