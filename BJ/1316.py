T = int(input())
result = T
for t in range(T):
    S = input()

    if len(S) == 1:
        continue

    for i in range(len(S)):
        if S[i] in S[i+2:] and S[i] != S[i+1]:
            result -= 1
            break

print(result)