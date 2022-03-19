for t in range(int(input())):
    n = int(input())
    ara = list(map(int,input().split()))
    c = 0
    for i in range(1,n-1):
        if (ara[i]>ara[i+1] and ara[i]>ara[i-1]):
            c = 1
            print("YES")
            print(i,i+1,i+2)
            break
    if c == 0:
        print("NO")



