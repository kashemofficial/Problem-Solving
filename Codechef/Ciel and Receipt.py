for i in range(int(input())):
    n=int(input())
    m=0
    for j in range(11,-1,-1):
        c=n//(2**j)
        m+=c
        n=n%(2**j)
    print(m)

