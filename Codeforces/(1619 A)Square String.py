for _ in range(int(input())):
    a = input()
    n = len(a)
    if n%2 != 0:
        print('NO')
    else:
        if a[:n//2] == a[n//2:]:
            print('YES')
        else:
            print('NO')

