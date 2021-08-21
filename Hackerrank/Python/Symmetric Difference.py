m = int(input())
M = set(list(map(int,input().split())))
n = int(input())
N = set(list(map(int,input().split())))
_set = sorted(list(M.difference(N)) + list(N.difference(M)))
print(*_set,sep='\n')




