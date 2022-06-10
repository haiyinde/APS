def recur_fact(num):
    # num == 1로 하게되면 recur_fact(0)일 때를 받지못해 지속적으로 num-=1이 되어 recursion error 발생
    if num <= 1:
        return 1
    return num*recur_fact(num-1) 

N = int(input())
print(recur_fact(N))
