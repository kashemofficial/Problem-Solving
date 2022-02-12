def solve(n):
    li = list()
    for c in n:
        if c in '(':
            li.append(c)
        elif c in ')':
            if not li:
                return False
            li.pop()
    return not li

if __name__ == '__main__':
    n = input()
    if solve(n):
        print('Yes')
    else:
        print('No')

