x, y, n = map(int, input().split())
box = [[0 for _ in range(y)] for _ in range(x)]
for _ in range(n):
    a, b = map(int, input().split())
    box[a - 1][b - 1] = 1
table = [0] * 10
for i in range(x - 2):
    for j in range(y - 2):
        total = sum(box[i][j:j + 3]) + sum(box[i + 1][j:j + 3]) + sum(box[i + 2][j:j + 3])
        table[total] += 1

[print(a) for a in table]