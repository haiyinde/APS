K = int(input())
data = [list(map(int, input().split())) for _ in range(6)]

big_width = 0
big_height = 0

for i in range(6):
    d, length = data[i][0], data[i][1]
    if (d == 1 or d == 2) and big_width < length:
        big_width = length
        wi = i
    elif (d == 3 or d == 4) and big_height < length:
        big_height = length
        hi = i

small_width = abs(data[(hi+1)%6][1] - data[(hi-1)%6][1])
small_height = abs(data[(wi+1)%6][1] - data[(wi-1)%6][1])

result = (big_height*big_width - small_height*small_width) * K

print(result)