def _Sum(arr):
    sum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j]
                       + arr[i + 2][j + 1] + arr[i + 2][j + 2])
    print(max(sum))
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().split())))
    _Sum(arr)



