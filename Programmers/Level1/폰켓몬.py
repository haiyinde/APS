def solution(nums):
    total_kinds = len(set(nums))
    pick = len(nums) / 2
    answer = min(total_kinds, pick)
    return answer

# Set 생각 못하고 BFS로 풀어야 하는 문제인가 했다. 삽질할뻔!