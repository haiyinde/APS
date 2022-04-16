A = N = input()
cycle = 0

if int(N) < 10:
    A = "0" + N

while int(A) != int(N) or cycle == 0:
    cycle += 1
    tmp = str(int(A[0]) + int(A[1]))
    A = A[-1] + tmp[-1]
print(cycle)