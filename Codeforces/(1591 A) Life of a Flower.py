for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    r = 0
    ans = 1
    if arr[0] == 1:
        ans += 1

    for i in range(1,n):
        if arr[i-1] == 1 and arr[i] == 1:
            ans+=5
        elif arr[i-1] == 0 and arr[i] == 1:
            ans += 1
        elif arr[i-1] == 0 and arr[i] == 0:
            r += 1
    if r:
        print(-1)
    else:
        print(ans)


