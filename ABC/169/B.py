N = int(input())
A = list(map(int,input().split()))
over_value = 10 ** 18 + 1
total = 1
cnt = 0
while cnt < len(A):
    total *= A[cnt]
    cnt += 1
    
if total >= over_value:
    total = -1
print(total)