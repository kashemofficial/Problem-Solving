for t in range(int(input())):
	y=int(input())
	l=list(map(int,input().split()))
	a=max(l)
	l.remove(a)
	b=sum(l)/(len(l))
	s=a+b
	print("%.9f"%s)

