class Stair_case:
    def __init__(self,n):
        self.n = n
        for i in range(1,n+1):
            print(" "*(n - i) + ('#'*i))

if __name__ == '__main__':
    n = int(input())
    Stair_case(n)