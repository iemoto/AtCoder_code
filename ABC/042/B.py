n, l = map(int,input().split())
s = []
[s.append(input()) for _ in range(n)]
s.sort()
print(''.join(s))