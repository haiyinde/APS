# D2
import sys
sys.stdin = open("input.txt", "r")
 
T = int(input())
for t in range(1, T+1):
    _ = int(input())
    scores = list(map(int, input().split()))

    print("#{} {}".format(t, max(set(scores), key=scores.count)))
