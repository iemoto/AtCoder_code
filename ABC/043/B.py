S = input()
stack = []
for ss in S:
    if ss == '0':
        stack.append(ss)
    elif ss == '1':
        stack.append(ss)
    elif ss == 'B':
        if len(stack):
            stack.pop()

print(''.join(stack))