def diagonalDifference(arr):
    a,b = 0,0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][-i-1]
    return abs(a-b)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    result = diagonalDifference(arr)
    print(result)