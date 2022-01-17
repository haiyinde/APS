# Queue, B1
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque([i for i in range(1, N+1)])

# 카드가 한 장 남을 때까지 반복 while len(queue) >= 2:
while len(Q) >= 2:
# 제일 위에 있는 카드를 바닥에 버린다 popleft
    print(Q.popleft(), end=' ')
# 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다. popleft -> append
    Q.append(Q.popleft())

# ground = 버린 카드들을 순서대로 출력하라.
print(Q[0])
