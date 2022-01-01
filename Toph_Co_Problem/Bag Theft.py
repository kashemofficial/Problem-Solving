def solve_e(st,ho,mi):
    result = ((ho - 9) * 60) + mi
    print(((result // 5) * 8) - ((result // 15) * 8))
if __name__ == '__main__':
    for _ in range(int(input())):
        st = input()
        ho = int(st[0:2])
        mi = int(st[2:])
        solve_e(st,ho,mi)
        