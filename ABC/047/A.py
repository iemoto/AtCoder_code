A, B, C = map(int,input().split())
x = max(A,B,C)
y = sum([A,B,C]) - x

if x == y:
    print('Yes')
else:
    print('No')