N = int(input())  # 이닝 수

data = [list(map(int, input().split() )) for _ in range(N)]

# 한 이닝에 3 아웃이 발생하면 이닝이 종료되고, 두 팀이 공격과 수비를 서로 바꾼다.

# 가장 많은 득점을 하는 타순을 찾고, 그 때의 득점을 구해보자.

# 첫번째 선수는 4번 타자.

