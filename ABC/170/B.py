X, Y = map(int, input().split())
flag = 0
for i in range(0,X+1):
    total = i * 2 + (X - i) * 4
    if total == Y:
        flag = 1
        break
if flag:
    print('Yes')
else:
    print('No')