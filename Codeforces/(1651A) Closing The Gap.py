for _ in range(int(input())):
    n = int(input())
    li = map(int,input().split())
    s = sum(li)
    if s%n == 0:
        print('0')
    else:
        print('1')