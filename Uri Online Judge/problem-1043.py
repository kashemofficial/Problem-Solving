a,b,c = list(map(float,input().split()))
if (a< b+c and b < a+c and c < a+b):
    print('Perimetro = %.1f'%(a+b+c))
else:
    print('Area = %.1f'%(c*(a+b)/2))


