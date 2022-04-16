N = int(input())
current_scores = list(map(int, input().split()))
M = max(current_scores)
new_scores = [score/M*100 for score in current_scores]
print(sum(new_scores)/N)