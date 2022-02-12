def solve(arr):
	c = arr.count('C')
	n = arr.count('N')
	d = arr.count('D')
	c = c + d
	n = n + d
	if c > n:
		return a*60
	elif c < n:
		return a*40
	else:
		return a*55
if __name__ == '__main__':
	for t in range(int(input())):
		a = int(input())
		arr = list(input())
		result = solve(arr)
		print(result)

