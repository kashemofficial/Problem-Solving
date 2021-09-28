for t in range(int(input())):
    s = input()
    a = 0
    b = 0
    c = 0
    for i in range(0,len(s)):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        else:
            c += 1
    if (b==(a+c)):
        print('YES')
    else:
        print('NO')