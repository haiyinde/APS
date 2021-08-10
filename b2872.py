import sys
n=int(input())
cnt = 0
L=[int(sys.stdin.readline())]
max = L[0]
for i in range(1,n):
 L.append(int(sys.stdin.readline()))
for i in range(1,n) :
 if L[i] > max :
   if max+1 != L[i] :
     cnt +=1
   max = L[i]
 else :
   cnt +=1
print(cnt)