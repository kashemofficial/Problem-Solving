'''for t in range(int(input())):
    a,b = map(int,input().split())
    s = ""
    res1 = (a+b)
    res2 = abs(a-b)
    for i in res1,res2:
        s +=str(i)
    print('Case %d:'%(t+1),s)'''

def solve(t,a,b):
    res1 = (a+b)
    res2 = (a-b)
    result = (res1,res2)
    print('Case %d: '%(t+1),*result,sep='')

if __name__ == '__main__':
    for t in range(int(input())):
        a,b = map(int,input().split())
        solve(t,a,b)





