score = int(input())

if score >= 90:
    result = "A"
elif 80 <= score <= 89:
    result = "B"
elif 70 <= score <= 79:
    result = "C"
elif 60 <= score <= 69:
    result = "D"
else:
    result = "F"

print(result)