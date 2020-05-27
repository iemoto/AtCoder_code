N = int(input())
S = list(map(int,input().split()))
ave = round(sum(S) / len(S))
ans = 0
for i in S:
    if i == ave:
        continue
    else:
       ans += (i - ave) ** 2

print(ans)