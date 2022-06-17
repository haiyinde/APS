def solution(n: int, plans: list, clients: list):
    def check_plan(data: int, add: list):
        for k, v in plan_data_dict.items():
            flag = True
            if v >= data:
                for a in add:
                    if a not in plan_add_dict[k]:
                        flag = False

                    if not flag:
                        break
                if flag:
                    return k
        return 0
    answer = [0] * len(clients)
    plan_data_dict = dict()
    plan_add_dict = dict()

    for i in range(len(plans)):
        plan = list(map(int, plans[i].split()))
        plan_data_dict[i+1] = plan[0]
        plan_add_dict[i+1] = plan[1:]

    for k, v in plan_add_dict.items():
        if k >= len(plans):
            break
        plan_add_dict[k+1] = v + plan_add_dict[k+1]

    for i in range(len(clients)):
        info = list(map(int, clients[i].split()))
        answer[i] = check_plan(info[0], info[1:])

    return answer


n1 = 5
plans1 = ["100 1 3", "500 4", "2000 5"]
clients1 = ["300 3 5", "1500 1", "100 1 3", "50 1 2"]

print(solution(n1, plans1, clients1))