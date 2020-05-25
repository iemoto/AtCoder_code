K, N = map(int, input().split())
liked_num = [0,1,2,3,4,5,6,7,8,9]
disliked_num = list(map(int, input().split()))
for s in disliked_num:
    liked_num.remove(s)
cnt = K
flag = 1
while flag:
    not_n = 1
    for i in str(cnt):
        if not int(i) in liked_num:
            not_n = 0
            break
    if not_n:
        break
    cnt += 1
print(cnt)