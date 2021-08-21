T = int(input())
for _ in range(T):
    n = int(input())
    product = 1
    sum = 0
    for j in range(1,n+1):
        product *= j
        sum += j/product
    print("%.4f"%sum)