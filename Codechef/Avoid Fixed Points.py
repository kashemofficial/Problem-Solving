for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(len(arr)):
        if arr[i] == (i+ans+1):
            ans += 1
    print(ans)

