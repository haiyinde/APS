def solution(s):
    lst = []
    answer = []
    s = s[2:-2]
    tmp = s.split("},{")
    # tmp_lst = []
    tmp.sort(key=lambda x: len(x))
    for element in tmp:
        e = element.split(",")
        # print(e)
        for j in e:
            intj = int(j)
            if intj not in lst:
                lst.append(intj)

    return lst



input1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
input2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
input3 = "{{20,111},{111}}"
input4 = "{{123}}"
input5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

# print(solution(input1))
print(solution(input2))
# print(solution(input3))
# print(solution(input4))
# print(solution(input5))
