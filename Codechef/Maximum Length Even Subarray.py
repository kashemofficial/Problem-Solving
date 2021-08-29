
for t in range(int(input())):
    n = int(input())
    if ((n%4 == 0) or (n+1)%4 == 0):
        print(n)
    else:
        print(n-1)