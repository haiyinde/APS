N = int(input())

def tower_of_hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    tower_of_hanoi(n-1, start, 6-start-end)
    print(start, end)
    tower_of_hanoi(n-1, 6-start-end, end)

print(2**N-1)
tower_of_hanoi(N, 1, 3)