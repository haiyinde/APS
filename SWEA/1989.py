# 1989
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    s = input()
    flag = 1
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            flag = 0
    print("#{} {}".format(t, flag))