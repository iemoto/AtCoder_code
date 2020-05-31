N = int(input())
n = round(N ** 0.5)
Z = N
cnt = 0
for i in range(2,n+1):
    if Z == 1:
        break
    if Z % i == 0:
        Z = Z // i
        cnt += 1
if cnt == 0 and Z > 1:
    cnt = 1

print(cnt)