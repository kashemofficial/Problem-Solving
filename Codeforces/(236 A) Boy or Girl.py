def solve(n):
    ans = dict.fromkeys(n)
    if len(ans)%2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
if __name__ == '__main__':
    n = input()
    solve(n)

