def lonelyinteger(a):
    answer = 0
    for candidate in a:
        answer ^= candidate
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int,input().strip().split(" "))
    print(lonelyinteger(b))
    


