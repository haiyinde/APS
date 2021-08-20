# 스택이랑 너무 헷갈린다 :(

import sys
input = sys.stdin.readline

def push(item):
    queue.insert(0, item)  # FIFO 이기때문에 append가 아니라 insert(위치, item)
    # .insert(i, x)
    # 정해진 위치 i에 값 x를 추가함 , 맨뒤에 넣을거면 len(), 리스트 길이보다 큰 경우 자동으로 맨뒤로 감


def pop():
    if len(queue) != 0:
        return queue.pop()  # 첫번째 값을 빼는 게 아니라 마지막값 빼는 거임..
    else:
        return -1


def size():
    return len(queue)


def empty():
    if len(queue):
        return 0
    else:
        return 1


def front():
    if len(queue):
        return queue[-1]  # 마지막껄 출력해줘야 처음 더해진 게 나옴
    else:
        return -1


def back():
    if len(queue):
        return queue[0]  # 처음껄 출력해줘야 마지막에 더해진 게 나옴
    else:
        return -1


N = int(input())
queue = []  # 그냥 빈칸으로 둬야한다.

for _ in range(N):

    order = input().split()  # list로 안해줘도 됨

    if order[0] == 'push':
        number = order[1]
        push(number)

    elif order[0] == 'pop':
        print(pop())

    elif order[0] == 'size':
        print(size())

    elif order[0] == 'empty':
        print(empty())

    elif order[0] == 'front':
        print(front())

    elif order[0] == 'back':
        print(back())

    else:  # 필요없지만...
        print('저장되지 않은 명령어입니다')
