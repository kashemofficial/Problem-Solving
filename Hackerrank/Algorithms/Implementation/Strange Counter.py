'''def solve(t):
    a = 3
    while t>a:
        t = t - a
        a = a*2
    print(a - t+1)

if __name__ == '__main__':
    t = int(input())
    solve(t)'''
t = int(input())
a = 3
for i in range(t>a):
    t-=a
    a *= 2
print(a - t+1)



