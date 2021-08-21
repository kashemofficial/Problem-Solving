def findMedian(arr):
    arr = sorted(arr)
    print(arr[len(arr)//2])
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int,input().split()))
    result = findMedian(arr)