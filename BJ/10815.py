import sys
input = sys.stdin.readline

N = int(input())
groupA = set(map(int, input().split()))
M = int(input())
groupB = list(map(int, input().split()))

for card in groupB:
    if card in groupA:
        print("1", end=" ")
    else:
        print("0", end=" ")