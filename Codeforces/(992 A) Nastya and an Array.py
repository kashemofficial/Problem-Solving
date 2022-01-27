n = input()
a = map(int,input().split())
result = len(set(a)-{0})
print(result)