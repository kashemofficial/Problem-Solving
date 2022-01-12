d,n = map(int,input().split())
arr = list(map(int,input().split()))
res = arr[n:]+arr[:n]
print(*res)




