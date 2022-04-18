S = list(input())
result = 0

for s in S:
    if 65 <= ord(s) <= 67:
        result += 3
    elif 68 <= ord(s) <= 70:
        result += 4
    elif 71 <= ord(s) <= 73:
        result += 5
    elif 74 <= ord(s) <= 76:
        result += 6
    elif 77 <= ord(s) <= 79:
        result += 7
    elif 80 <= ord(s) <= 83:
        result += 8
    elif 84 <= ord(s) <= 86:
        result += 9
    elif 87 <= ord(s) <= 90:
        result += 10

print(result)