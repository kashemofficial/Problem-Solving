a,b,c,d = map(int,input().split())
m_in = min(a,c,d)
print((256*m_in) + (32*min(a-m_in,b)))
