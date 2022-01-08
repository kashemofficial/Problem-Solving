for _ in range(int(input())):
    n,m,s = list(map(int,input().split()))
    result = (s-1+m-1)%n
    print(result+1)
