N = int(input())
A = list(map(int,input().split()))
over_value = 10 ** 18
total = 1
cnt = 0
while cnt < N:
    total *= A[cnt]
    if total > over_value:
        total = -1
        break
    cnt += 1
    
for i in range(N):
    if A[i] == 0:
        total = 0
print(total)