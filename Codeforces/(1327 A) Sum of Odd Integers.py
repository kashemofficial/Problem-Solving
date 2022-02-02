for i in range(int(input())):
    n, k = map(int, input().split())
    if k * k <= n and n % 2 == k % 2:
        print('YES')
    else:
        print('NO')

