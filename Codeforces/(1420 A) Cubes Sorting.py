for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	co = False
	for i in range(1,n):
		if arr[i]>=arr[i-1]:
			co = True
	if co:
		print("YES")
	else:
		print("NO")
