S = input().upper()
set_S = list(set(S))
most = []
for s in set_S:
    most.append(S.count(s))
if most.count(max(most)) >= 2:
    print("?")
else:
    print(set_S[most.index(max(most))])
