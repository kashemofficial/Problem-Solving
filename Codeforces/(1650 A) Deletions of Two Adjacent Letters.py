def solve(s1,s2):
    c = 0
    li = []
    for i in s1:
        c+=1
        if s2 == i:
            li.append(c)
    ans = 0
    for j in li:
        if j%2 != 0:
            ans += 1
    if ans>0:
        return 'YES'
    else:
        return "NO"
if __name__ == '__main__':
    for t in range(int(input())):
        s1 = str(input())
        s2 = str(input())
        res = solve(s1,s2)
        print(res)