import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_number = dict()
pokemon_name = dict()  # 메모리를 두 배로 사용한다는 단점이 있지만 빠름.

for i in range(1, N+1):
    pokemon_number[i] = input().strip()

for k, v in pokemon_number.items():
    pokemon_name[v] = k

for _ in range(M):
    quiz = input().strip()
    if quiz.isalpha():
        print(pokemon_name[quiz])
    elif quiz.isnumeric():
        print(pokemon_number[int(quiz)])