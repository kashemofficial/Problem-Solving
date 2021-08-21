def insertion_sort(t,arr):
    n = len(arr)
    for i in range(1,n):
        item = arr[i]
        j = i-1
        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j - 1
            arr[j+1] = item
        print(*arr)
if __name__ == '__main__':
    t = int(input())
    arr = list(map(int,input().split()))
    insertion_sort(t,arr)