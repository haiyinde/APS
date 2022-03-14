# D2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    commands = [list(map(int, input().split())) for _ in range(N)]
    length = 0
    velocity = 0
    for c in commands:
        if c[0] == 0:  # 유지
            length += velocity
        elif c[0] == 1:  # 가속
            velocity += c[1]
            length += velocity
        elif c[0] == 2:  # 감속
            if velocity < c[1]:
                velocity = 0
            else:
                velocity -= c[1]
            length += velocity

    print("#{} {}".format(t, length))