def solve(n):
    m = min(n)
    result = n.replace(m,"",1)
    print(m,result)
if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        solve(n)

