import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    words = input()
    for i in range(1, 10):
        if words[:i] == words[i:2*i]:
            print("#{} {}".format(test_case, i))
            break


# while문문
# for t inrange(1, int(input())+1):
#     s = input()
#     i = 1
#     while s[:i] != s[i:2*i]:
#         i += 1
#     print("#{} {}".format(t, i))