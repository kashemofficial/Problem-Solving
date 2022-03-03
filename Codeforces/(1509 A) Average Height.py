for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in arr:
        if i%2:
            print(i,end=" ")

    for i in arr:
        if (i % 2 == 0):
            print(i,end=" ")
    print()