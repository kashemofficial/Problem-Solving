for _ in range(int(input())):
    n = input()
    s1 = n.count('0')
    s2 = n.count('1')
    if s1!=s2:
        print(min(s1,s2))
    else:
        print((len(n)-1)//2)



