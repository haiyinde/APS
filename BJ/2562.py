numbers = []
for i in range(9):
    numbers.append(int(input()))
print(max(numbers), numbers.index(max(numbers))+1)