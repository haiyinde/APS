# D3
import sys
sys.stdin = open("input.txt", "r")

def dfs(count):
    global answer

    if not count:
        tmp_max = int("".join(numbers))
        if answer < tmp_max:
            answer = tmp_max
        return

    for i in range(L):
        for j in range(i+1, L):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            tmp = "".join(numbers)
            # .get(key[, default])
            if visited.get((tmp, count-1), 1):
                visited[(tmp, count-1)] = 0
                dfs(count-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())
for t in range(1, T+1):
    numbers, switch = input().split()
    # 교환 편의를 위해 list로 변형
    numbers = list(numbers)
    # switch는 int 재귀에서 숫자로 세야하므로 int로 변형
    switch = int(switch)
    L = len(numbers)
    visited = {}
    answer = -1
    dfs(switch)

    print("#{} {}".format(t, answer))

# T = int(input())
# for tc in range(1, T + 1):
#     num, N = input().split()
#     ans = set()
#     ans.add(num)
#     nxt = set()
#
#     for _ in range(int(N)):
#         while ans:
#             s = list(ans.pop())
#             for j in range(len(num)):
#                 for k in range(j + 1, len(num)):
#                     s[k], s[j] = s[j], s[k]
#                     nxt.add(''.join(s))
#                     s[k], s[j] = s[j], s[k]
#         nxt, ans = ans, nxt
#
#     print(f'#{tc} {max(map(int, ans))}')