def solution(a, b):
    answer = ''
    total_days = 0
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    monthes = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for m in range(1, a):
        total_days += monthes[m]

    total_days += b - 1
    day = total_days % 7
    return days[day]