for i in range(int(input())):
    x = input()
    y = input()
    l = y[::-1].index('1')
    r = x[::-1].index('1',l,len(x))
    print(r-l)
