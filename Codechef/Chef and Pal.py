for i in range(int(input())):
    n = int(input())
    if n%2 == 0:
        print('1'*(n//2),'0'*(n//2),sep='')
    else:
        print(-1)


