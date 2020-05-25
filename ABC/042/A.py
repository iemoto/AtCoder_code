input_575 = list(map(int, input().split()))
li_575 = [5, 7, 5]
for i in input_575:
    if i in li_575:
        li_575.remove(i)
if len(li_575) == 0:
    print('YES')
else:
    print('NO')