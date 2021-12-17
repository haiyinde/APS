k = int(input())
signes = list(input().split())
used = [False]*10
mx, mn = "", ""

def possible(i,j,k): # 가능한지 불가능한지 판단해주는 함수
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def solve(cnt, s):

    global mx, mn
    if cnt == k+1:
        if not len(mn): # mn이 비워져 있으면 최솟값에 s 넣기
            mn = s
        else: # mn에 값이 있으면 최댓값에 넣기
            mx = s
        return
    for num in range(10):
        if not used[num]:
            if cnt == 0 or possible(s[-1], str(num), signes[cnt-1]):
                used[num] = True
                solve(cnt+1, s+str(num))
                used[num] = False


solve(0, "")
print(mx)
print(mn)