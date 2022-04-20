# 다시 풀어보기
N = int(input())
room = 1  # 벌집의 방. 중앙의 1부터 시작
layer = 1  # 벌집의 층계

while N > room:
    room += 6*layer
    layer += 1

print(layer)