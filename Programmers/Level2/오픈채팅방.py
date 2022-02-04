def solution(record):
    answer = []
    user_book = {}
    for message in record:
        pieces = message.split()
        if pieces[0] == "Enter" or pieces[0] == "Change":
            user_book[pieces[1]] = pieces[2]

    for message in record:
        pieces = message.split()
        if pieces[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user_book[pieces[1]]))
        elif pieces[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(user_book[pieces[1]]))
    return answer
