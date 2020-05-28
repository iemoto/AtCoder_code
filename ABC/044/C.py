N, A = map(int,input().split())
numbers = list(map(int,input().split()))
how_many = 0
for i in range(1 << N):
    total = 0
    cnt = 0
    for j in range(N):
        if (i >> j)&1:
            cnt += 1
            total += numbers[j]
            
    if cnt > 0:
        average = total / cnt
        if average == float(A):
            how_many += 1
print(how_many)