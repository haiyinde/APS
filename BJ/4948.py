prime_numbers = []

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

candidates = list(range(2, 246912))
results = []

for i in candidates:
    if isPrime(i):
        results.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for pn in results:
        if n < pn <= 2*n:
            cnt += 1

    print(cnt)
