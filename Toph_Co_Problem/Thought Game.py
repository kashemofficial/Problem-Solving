for t in range(int(input())):
    a,b = map(int,input().split())
    res = (int(a)+int(b))//2
    if res%2 == 0:
        print('Sadia will be happy.')
    else:
        print('Oops!')
