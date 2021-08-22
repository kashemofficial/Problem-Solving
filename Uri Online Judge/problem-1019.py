N = int(input())
A = [3600,60,1]
M = []
for i in A:
    J =int(N/i)
    M.append(str(J))
    N -= J*i
print(":".join(M))
