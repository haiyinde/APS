import sys
input = sys.stdin.readline # 반복문으로 여러줄 입력받는 상황에서는 필수

def isPalindrome(a):
    return a[::-1] == a

def isPseudoPalindrome(a):
    if len(a) == 2:
        return True

    if isPalindrome(a[1:]) or isPalindrome(a[:-1]):
        return True

    if a[0] != a[-1]:
        return False

    diff_i = 1
    for i in range(1, len(a)//2):
        if a[i] != a[~i]:  # S[len(s)-1-i] == S[~i]
            diff_i = i
            break

    return isPseudoPalindrome(a[diff_i:~diff_i+1])

T = int(input())  # 문자열의 개수 T 1 <= T <= 30

for _ in range(T):
    s = input().rstrip()
    result = 2
    if isPalindrome(s):
        result = 0
    elif isPseudoPalindrome(s):
        result = 1

    print(result)