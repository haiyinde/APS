n = int(input())

def fibo_reg(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_reg(num-1) + fibo_reg(num-2)

result = fibo_reg(n)
print(result)