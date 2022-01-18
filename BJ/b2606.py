# BFS, S3
import sys
input = sys.stdin.readline

V = int(input())  # V <= 100
E = int(input())

# 인접 딕셔너리
node = { i : [] for i in range(V+1)}
for _ in range(E):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

visited = [False] * (V+1) # 방문체크
queue = [] # 다음 탐색할 지점을 저장할 queue
queue.append(1)  # 시작점 넣어주기
result = 0 # 정답 변수

while queue:  # 모든 경우의 수를 다 봤다면 탈출
    t = queue.pop(0)
    # t는 현재 방문중인 지점
    # popleft -> 제일 먼저 탐색할 지점 꺼내기

    if not visited[t]:  # 안가본 곳이면
        visited[t] = True  # 방문체크
        result += 1  # 연결된 컴퓨터

    for i in node[t]: # 현재 방문한 곳과 연결된 지점 탐색
        if not visited[i]:  # 방문 안해본 곳이면
            queue.append(i)  # 방문해야하니까 줄 세우기

print(result-1)  # 최초에 시작할 때 +1이 되었으므로 -1