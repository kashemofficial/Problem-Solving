def closestNumbers(arr):
    li = []
    arr = sorted(arr)
    mind = float("inf")
    for i in range(len(arr) - 1):
        v1 = arr[i]
        v2 = arr[i + 1]
        if v2 - v1 < mind:
            li = []
            mind = v2 - v1
        if v2 - v1 <= mind:
            li.append(v1)
            li.append(v2)
    return li
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(*result)
