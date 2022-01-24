a=int(input())
b=str(bin(a))
c=b[2:]
d=c.replace("0","")
e=int(d,2)
print(e)
