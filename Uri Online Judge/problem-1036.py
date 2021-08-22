import math
a,b,c = map(float,input().split())
sroot = ((b**2)- 4*a*c)
if sroot<0 or a == 0:
    print("Impossivel calcular")
else:
    n = math.sqrt(sroot)
    r1 = ((-b+n)/(2*a))
    r2 = ((-b-n)/(2*a))
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)
