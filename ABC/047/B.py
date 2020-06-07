X, Y, N = map(int, input().split())
canvas = [[1 for _ in range(X)]for _ in range(Y)]

for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        for j in range(Y):
            for k in range(x):
                canvas[j][k] = 0
    if a == 2:
        for j in range(Y):
            for k in range(x,X):
                canvas[j][k] = 0
    if a == 3:
        for j in range(X):
            for k in range(y):
                canvas[k][j] = 0
    if a == 4:
        for j in range(X):
            for k in range(y,Y):
                canvas[k][j] = 0
print(sum([sum(i) for i in canvas]))
