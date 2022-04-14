H, M = map(int, input().split())

if M >= 45:
    M -= 45
else:
    H -= 1
    M += 60 - 45

if H <= -1:
    H += 24

print(H, M)