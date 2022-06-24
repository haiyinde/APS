def solution(a, b, c, d, e, f):
    beads = [a-d, b-e, c-f]
    leftover = 0

    for bead in beads:
        if bead >= 0:
            leftover += bead//2
        else:
            leftover += bead

    return True if leftover >= 0 else False


print(solution(4, 4, 2, 2, 2, 0))
print(solution(3, 3, 3, 1, 1, 4))
print(solution(2, 2, 1, 1, 1, 2))