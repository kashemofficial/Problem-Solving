n = int(input())
mod = 1000000007
c1 = 6
c2 = 16
for i in range(1,n):
    c1 = c1*c2%mod
    c2 = c2*c2%mod
print(c2)

