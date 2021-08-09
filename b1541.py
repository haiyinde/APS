list_a = input().split('-') # '-' 뒤의 숫자를 괄호로 묶으면 최솟값이 나온다. 따라서 -를 기준으로 나눈 list_a를 생성

total = 0
for i in list_a[0].split('+'): # -가 나오기 전까지의 str 숫자 리스트. 쪼개서 더해줘야한다
    total += int(i)

for i in list_a[1:]: # -가 나온 이후의 str 숫자 리스트.
    for j in i.split('+'): # +를 기준으로 숫자로 나누어 준 후, 
        total -= int(j) # total 값에서 빼준다.

print(total)
