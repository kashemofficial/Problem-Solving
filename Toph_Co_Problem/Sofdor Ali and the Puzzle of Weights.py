for _ in range(int(input())):
    w = int(input())
    weights = []
    i = 0
    while sum(weights) < w:
        weights.append(3 ** i)
        i+=1
    res = len(weights)
    print('Case %d: %d'%(_+1,res))
