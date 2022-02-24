def solution(id_list, reports, k):
    answer = []
    blocked_user = []
    reported_num = 0
    reported_dict = {}
    reportees = []
    for report in reports:
        reporter, reportee = report.split(" ")
        # print(reporter, reportee)
        reportees.append(reportee)
        # reported_dict[reportee] = 0
    # print(reportees)

    for reportee in reportees:
        reported_dict[reportee] = reportees.count(reportee)
    print(reported_dict)

    # if reported_num >= k:
    #     blocked_user.append(user)

    return answer

id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2
id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
print(solution(id_list1, report1, k1))
print(solution(id_list2, report2, k2))