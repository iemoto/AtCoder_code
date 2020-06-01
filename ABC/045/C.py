S = input()
n = len(S) - 1
total = 0
for i in range(1 << n):
    t = S[0]
    for j in range(n):
        if (i >> j) & 1:
            t += '+' + S[j + 1]
        else:
            t += S[j + 1]
    total += eval(t)

print(total)