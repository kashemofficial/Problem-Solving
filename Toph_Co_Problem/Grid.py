for t in range(int(input())):
    a,b = map(int,input().split())
    print('Case %d:'%(t+1))
    for i in range(a):
        for j in range(b):
            print('*',end='')
        print()

