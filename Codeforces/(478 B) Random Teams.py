n,m = map(int,input().split())
a = n//m
b = n%m
max = (n-m)*(n-m+1)//2
min = ((a*(a+1)*b)//2)+((a-1)*a*(m-b)//2)
print(min,max)


