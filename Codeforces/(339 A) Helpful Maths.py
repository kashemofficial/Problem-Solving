def solve(a):
    a.sort()
    res = ''
    for i in a:
        res+=i+'+'
    print(res[:-1])
if __name__ == '__main__':
    a = input().split('+')
    solve(a)

