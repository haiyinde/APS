from collections import defaultdict

def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    reported_dict = {}
    blocked_users = []
    # 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리
    reports = list(set(reports))
    reports_data = defaultdict(list)
    for id in id_list:
        reported_dict[id] = 0
    for report in reports:
        reporter, reportee = report.split(" ")
        reported_dict[reportee] += 1
        reports_data[reporter].append(reportee)
    # print(reports_data)
    for id in id_list:
        if reported_dict[id] >= k:
            blocked_users.append(id)

    for bu in blocked_users:
        for i in range(len(id_list)):
            if bu in reports_data[id_list[i]]:
                answer[i] += 1
    # print(blocked_users)
    return answer

id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2
id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
print(solution(id_list1, report1, k1))
print(solution(id_list2, report2, k2))