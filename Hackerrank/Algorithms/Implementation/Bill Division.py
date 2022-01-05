n,k = map(int,input().split())
bill = list(map(int,input().split()))
b = int(input())
sum = sum(bill)-bill[k]
res = sum//2
if res == b:
    print('Bon Appetit')
else:
    print(b - res)


'''def solve(k,bill,b):
    s = sum(bill)-bill[k]
    res = s//2
    if res == b:
        print('Bon Appetit')
    else:
        print(b-res)

if __name__ == '__main__':
    n,k = map(int,input().split())
    bill = list(map(int,input().split()))
    b = int(input())
    solve(k,bill,b)'''