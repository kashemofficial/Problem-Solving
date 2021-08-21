def insertion_sort(n,arr):
    a = n - 1
    val = arr[a]
    while (a > 0 and val < arr[a - 1]):
        arr[a] = arr[a - 1]
        print(*arr)
        a -= 1
    arr[a] = val
    print(*arr)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    insertion_sort(n,arr)

