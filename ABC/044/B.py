S = input()
str_box = {}
jodge = 1
for ss in S:
    if ss in str_box:
        str_box[ss] += 1
    else:
        str_box[ss] = 1
for i in str_box.values():
    if i % 2 != 0:
        jodge = 0
if jodge:
    print('Yes')
else:
    print('No')