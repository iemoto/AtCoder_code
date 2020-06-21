from itertools import combinations

N, K = map(int,input().split())
lists = combinations(range(N),K)
s = list(map(int,input().split()))
min_result = 1000000000000
for li in lists:
    total = 0
    for l in li:
        total += s[l]
    min_result = min(min_result,total)

print(min_result)