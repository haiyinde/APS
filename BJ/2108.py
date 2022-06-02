import sys
from collections import Counter

N = int(input())
numbers = list(int(sys.stdin.readline()) for _ in range(N))

print(round(sum(numbers)/N))
numbers.sort()
print(numbers[N//2])

modes = Counter(numbers).most_common()
if len(modes) >= 2 and modes[0][1] == modes[1][1]:
    print(modes[1][0])
else:
    print(modes[0][0])

print(max(numbers)-min(numbers))