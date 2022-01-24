arr = []
for _ in range(int(input())):
    x = input()
    if x in arr:
        print('YES')
    else:
        print('NO')
        arr.append(x)

