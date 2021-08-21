def runningTime(arr):
    return ([j for j in range(len(arr))for i in range(j,len(arr))if arr[j]>arr[i]])
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = runningTime(arr)
    print(len(result))