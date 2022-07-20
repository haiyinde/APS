def solution(brown, red):
    height = 3
    width = (brown+red) // height

    while (width-2) * (height-2) != red:
        width -= 1
        height = (brown+red) // width

    return [width, height]


def solution(brown, red):
    total = brown + red

    for h in range(3, int(total ** 0.5) + 1):
        w = total // h
        if total % h == 0 and (h - 2) * (w - 2) == red:
            return [w, h]