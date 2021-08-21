n = int(input())
arr = []
for _ in range(n):
    e = input().split()
    if e[0] == 'insert':
        arr.insert(int(e[1]),int(e[2]))
    elif e[0] == 'print':
        print(arr)
    elif e[0] == 'remove':
        arr.remove(int(e[1]))
    elif e[0] == 'append':
        arr.append(int(e[1]))
    elif e[0] == 'sort':
        arr.sort()
    elif e[0] == 'pop':
        arr.pop()
    else:
        arr.reverse()