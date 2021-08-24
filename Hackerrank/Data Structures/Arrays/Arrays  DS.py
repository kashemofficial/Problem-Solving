def reverseArray(arr):
    result = arr[::-1]
    print(*result)
if __name__=="__main__":
    a = int(input())
    arr = list(map(int,input().split()))
    reverseArray(arr)
