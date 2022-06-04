N = int(input())

def get_stars(step):
    if step == 1:
        return ["*"]
    stars = get_stars(step//3)
    canvas = []

    for star in stars:
        canvas.append(star*3)
    for star in stars:
        canvas.append(star+" "*(step//3)+star)
    for star in stars:
        canvas.append(star*3)

    return canvas

print("\n".join(get_stars(N)))