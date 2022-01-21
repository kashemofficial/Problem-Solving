def solve(arr):
    res = arr[::-1]
    print(*res)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    solve(arr)


