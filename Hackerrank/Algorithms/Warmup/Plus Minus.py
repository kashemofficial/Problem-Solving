def Plus_Minus(n,li):
    positive = sum(i>0 for i in li)
    negative = sum(i<0 for i in li)
    zero = sum(i==0 for i in li)
    print('%0.6f'%(positive/n))
    print('%0.6f'%(negative/n))
    print('%0.6f'%(zero/n))
if __name__ == '__main__':
    n = float(input())
    li = [float(j) for j in input().split()]
    Plus_Minus(n,li)
