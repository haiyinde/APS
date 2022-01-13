# DFS
def DFS(W=500, cnt=0):
    if cnt == N:  # cnt가 N일때 답을 내겠다.
        global result
        result += 1
        return

    for i in range(N):
        if not visited[i] and W - K + A[i] >= 500:  # 만약 방문하지 않았다면
            visited[i] = True
            DFS(W - K + A[i], cnt+1)
            visited[i] = False  # 재귀가 끝나고 돌아왔다면 방문체크 풀어주기



N, K = map(int, input().split())
A = list(map(int, input().split()))

# 재귀에서 무한루프 방지
visited = [False] * N

result = 0

DFS()
print(result)