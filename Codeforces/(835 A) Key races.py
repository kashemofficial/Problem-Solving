s,v1,v2,t1,t2=map(int,input("").split())
d=s*v1+t1*2
z=s*v2+t2*2
if d<z:
    print("First")
elif d>z:
    print("Second")
else:
    print("Friendship")

