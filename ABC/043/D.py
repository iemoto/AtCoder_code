S = input()
N = len(S)
for i in range(N-1):
    if S[i] == S[i + 1]:
        print(i+1,i+2)
        exit()
for i in range(N-2):
    if S[i] == S[i + 2]:
        print(i + 1 ,i + 3)
        exit()
        
print(-1,-1)