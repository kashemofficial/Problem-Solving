def solve(arr):
    arr.sort()
    print(sum(arr[:-1]),sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    solve(arr)
