for j in range(int(input())):
    t = int(input())
    li = []
    for i in range(t):
        li.append(float(input()))
    res = sum(li)/t
    print('Case %d: %.3f'%((j+1),res))


