N = int(input())
K = int(input())
price = int(input())
d_price = int(input())
if K >= N:
    total = N * price
    print(total)
else:
    total = K * price
    N -= K
    total += N * d_price
    print(total)
