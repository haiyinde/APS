S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = [-1 for _ in range(len(alphabet))]
for i in range(len(S)):
    for j in range(len(alphabet)):
        if S[i] in alphabet[j] and result[j] == -1:
            result[j] = i
print(" ".join(map(str, result)))