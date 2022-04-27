N = int(input())
M = int(input())
primes = []

for num in range(N, M+1):
    # 1은 소수가 아니다. 예외처리 빼먹음
    if num == 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))