for t in range(int(input())):
    n,a,b = map(int,input().split())
    c = 1
    for i in range(50):
        if c>n:
            print("NO")
            break
        if (n-c)%b == 0:
            print("YES")
            break
        else:
            c *= a
    else:
        print("NO")