def solve():
    for i in range(5):
        arr = [int(i) for i in input().split()]
        for j in range(5):
            if arr[j] == 1:
                print(abs(2-i)+abs(2-j))
                exit()
if __name__ == '__main__':
    solve()


