N = int(input())

line = 1
while N > line:
    N -= line
    line += 1

if line % 2 == 0:
    a = N
    b = line-N+1
else:
    a = line-N+1
    b = N
print(a, '/', b, sep='')