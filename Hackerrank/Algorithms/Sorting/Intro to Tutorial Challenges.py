def introTutorial(V,n,arr):
    return arr.index(V)

if __name__ == '__main__':
    V = int(input())
    n = int(input())
    arr = list(map(int,input().split()))
    result = introTutorial(V,n,arr)
    print(result)