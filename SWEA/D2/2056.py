# D1
calendar = {"01": list(range(1, 32)),
            "02": list(range(1, 29)),
            "03": list(range(1, 32)),
            "04": list(range(1, 31)),
            "05": list(range(1, 32)),
            "06": list(range(1, 31)),
            "07": list(range(1, 32)),
            "08": list(range(1, 32)),
            "09": list(range(1, 31)),
            "10": list(range(1, 32)),
            "11": list(range(1, 31)),
            "12": list(range(1, 32))}

T = int(input())
for test_case in range(1, T+1):
    dates = input()
    years = dates[:4]
    months = dates[4:6]
    days = dates[6:8]

    if not 1 <= int(months) <= 12:
        print("#{} -1".format(test_case))
        continue

    if int(days) not in calendar[months]:
        print("#{} -1".format(test_case))
        continue

    print("#{} {}/{}/{}".format(test_case, years, months, days))

