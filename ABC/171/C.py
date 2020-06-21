N = int(input()) - 1
flag = 1
box = []
while flag:
    if not N:
        break
    s = N % 26
    N = N // 26
    box.append(s)
print(box)
# [print(chr(i + 96)) for i in box]
    