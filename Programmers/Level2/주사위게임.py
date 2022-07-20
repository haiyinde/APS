from itertools import product

def solution(monster, S1, S2, S3):
    monster = set(monster)  # 해쉬화 : list를 in 사용하면 O(n)인데 set()하면 O(1)로 가능
    p = product(range(S1), range(S2), range(S3))
    # 딱히 list로 만들지 않아도, range로만 해도 된다.
    case = len([x for x in p if sum(x)+4 not in monster])
    return int(case / (S1*S2*S3) * 1000)


# def solution(monster: list, S1: int, S2: int, S3: int):
#     total = S1 * S2 * S3
#     chance_to_meet = 0
#
#     S1 = range(1, S1 + 1)
#     S2 = range(1, S2 + 1)
#     S3 = range(1, S3 + 1)
#
#     all_chances = list(product(*[S1, S2, S3]))
#
#     for a in all_chances:
#         if 1 + sum(a) in monster:
#             chance_to_meet += 1
#
#     not_metting = total - chance_to_meet
#     return int(not_metting / total * 1000)