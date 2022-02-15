class solution:
    def __init__(self,f):
        self.f = f
        n = f//10
        pl = '+'*n
        d = '.'*(10-n)
        p = f
        print("[{}{}] {}%".format(pl,d,p))

if __name__ == '__main__':
    f = int(float(input()))
    solution(f)

