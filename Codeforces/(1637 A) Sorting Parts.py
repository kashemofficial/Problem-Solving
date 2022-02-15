for t in range(int(input())):
    a = int(input())
    arr = list(map(int, input().split()))
    if arr == sorted(arr):
        print("NO")
    else:
        print("YES")

