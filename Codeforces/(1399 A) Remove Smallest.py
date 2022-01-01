for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int,input().split()))
    for i in range(1,n):
        if arr[i] - arr[i - 1] > 1:
            print('NO')
            break
    else:
        print('YES')