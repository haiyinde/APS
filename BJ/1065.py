N = int(input())
result = 0
for n in range(1, N+1):
    if n < 100:
        result += 1
    else:
        n = str(n)
        # 1000의 경우 if에서 false되어 자동으로 pass
        if int(n[1]) - int(n[0]) == int(n[2]) - int(n[1]): 
            result += 1

print(result)
