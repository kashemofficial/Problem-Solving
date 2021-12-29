n = int(input())
arr = sorted(list(map(int,input().split())))
left = 0
right = len(arr)
while left <= right:
    mid = (left+right)//2
    print(mid)
    break




