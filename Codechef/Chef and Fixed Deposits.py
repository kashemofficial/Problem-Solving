for _ in range(int(input())):
    n,x = map(int,input().split())
    li = list(map(int,input().split()))[:n]
    arr = sorted(li)[::-1]
    sum = 0
    c = 0
    for i in range(n):
        sum += arr[i]
        c += 1
        if sum >= x:
            print(c)
            break
    else:
        print(-1)

'''for _ in range(int(input())):
    n,x = map(int,input().split())
    li = list(map(int,input().split()))[:n]
    arr = sorted(li)[::-1]
    if arr[0]>=x:
        print(1)
    elif arr[0]+arr[1] >= x:
        print(2)
    else:
        print(-1)'''


