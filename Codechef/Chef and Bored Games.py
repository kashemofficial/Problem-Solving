class solve:
    def __init__(self,n):
        self.n = n
        c = 0
        for i in range(1,n+1,2):
            c+=(n-i+1)*(n-i+1)
        print(c)

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        solve(n)


'''for t in range(int(input())):
    n = int(input())
    c = 0
    for i in range(1,n+1,2):
        c += (n-i+1)*(n-i+1)
    print(c)'''
