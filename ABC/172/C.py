n,m,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
book_cnt = 0
flag = 1
while flag:
    if not A and not B:
        break
    
    if A[0] > B[0]:
        k -= A[0]
        A.pop(0)
        book_cnt += 1
    elif B[0] > A[0]:
        k -= B[0]
        B.pop(0)
        book_cnt += 1

                
        
print(book_cnt)
