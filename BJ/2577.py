A = int(input())
B = int(input())
C = int(input())
for i in range(10):
    print(list(str(A*B*C)).count(str(i)))