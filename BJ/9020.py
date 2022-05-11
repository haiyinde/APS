def isPrime(num):

    if num == 1:
        return False

    elif num == 2:
        return True

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

T = int(input())
for t in range(T):
    n = int(input())
    a = int(n / 2)
    b = int(n / 2)
    while True:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
