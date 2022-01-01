N = int(input())
n1 = 1
n2 = 1
for i in range(2,N):
    fibo = n1 + n2
    n1 = n2
    n2 = fibo
print(fibo)