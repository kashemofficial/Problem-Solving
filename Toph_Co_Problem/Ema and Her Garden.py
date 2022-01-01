def solve_c(str):
    em = set(str)
    if len(str) == len(em):
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    str = input()
    solve_c(str)
