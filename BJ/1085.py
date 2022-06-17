x, y, w, h = map(int, input().split())
left = x
top = y
right = w - x
bottom = h - y

print(min(left, top, right, bottom))