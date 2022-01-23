def solve(arr1,arr2):
    res = set(arr2)
    for j in range(len(arr1)):
        if arr1[j] in res:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    a,b = map(int,input().split())
    arr1 = input().split()
    arr2 = input().split()
    solve(arr1,arr2)

