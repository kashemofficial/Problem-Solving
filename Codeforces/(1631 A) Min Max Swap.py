for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            arr2[i],arr1[i] = arr1[i],arr2[i]
    print(max(arr1) *max(arr2))

