def DFS(time=0, now=0, snowball=1):
    global biggest
    if time > M:  # 시간이 다되어도 return => "=="이라고 했었음
        return

    if time <= M:
        biggest = max(biggest, snowball)

    if now <= N-1:
        DFS(time+1, now+1, snowball+a[now+1])

    if now <= N-2:
        DFS(time+1, now+2, snowball//2+a[now+2])



N, M = map(int, input().split())  # 앞마당의 길이 N 대회의 시간 M
a = [0] + list(map(int, input().split()))  # 수열 a, 시작위치는 0이다 ㅠㅠ

biggest = 0

DFS()

print(biggest)