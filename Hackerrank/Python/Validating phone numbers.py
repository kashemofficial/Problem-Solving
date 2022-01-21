for _ in range(int(input())):
    n = input()
    if(len(n)==10 and n[0] in ['9', '8', '7'] and n.isnumeric()):
        print("YES")
    else:
        print("NO")



