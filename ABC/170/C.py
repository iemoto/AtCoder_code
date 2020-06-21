abs, N = map(int,input().split())
flag = 0
if N:
    s = list(map(int,input().split()))
    flag = 1
cnt = 0
while flag:
    if not(abs - cnt) in s:
        result = abs - cnt
        break
    if not(abs + cnt) in s:
        result = abs + cnt
        break
    cnt += 1
if flag:
    print(result)
else:
    print(abs)