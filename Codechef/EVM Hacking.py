for t in range(int(input())):
    a ,b ,c ,p ,q , r =map(int ,input().split())
    h =( p + q +r ) /2
    s0 =float( a + b +c)
    s1 =float( p + b +c)
    s2 =float( a + q +c)
    s3 =float( a + b +r)
    if s1 >h or s2 >h or s3 >h:
        print("YES")
    else:
        print("NO")
