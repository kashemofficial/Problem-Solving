for t in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    c = 0
    for i in range(len(li)):
        if li[i] == 0:
            c+=1
    print(max(c,n-c))

