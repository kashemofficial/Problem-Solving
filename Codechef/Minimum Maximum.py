for _ in range(int(input())):
    n = int(input())
    arr = map(int,input().split())
    print(min(arr)*(n-1))
