# list comprehension
numbers = [int(input()) for i in range(9)]
print(max(numbers), numbers.index(max(numbers))+1)