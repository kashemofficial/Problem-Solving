for t in range(int(input())):
    n,k = map(int,input().split(' '))
    arr = list(map(int,input().split()))
    ans = 0
    mx = max(arr)
    for i in range(k-1,n):
        if arr[i] == mx:
            ans += n-i
    print(ans)