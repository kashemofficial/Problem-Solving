n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
s=sum(arr1)
arr2.sort(reverse=True)
if arr2[0]+arr2[1]>=s:
    print("YES")
else:
    print("NO")




