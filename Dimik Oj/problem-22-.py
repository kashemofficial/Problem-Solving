""""T = int(input())
for i in range(T):
    a,b=map(int,input().split())
    count = []
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if (num%i) == 0:
                    break
            else:
                count.append(i)
        print(len(count))"""


def prime_numbers(a,b):
    li = [False if x % 2 == 0 else True for x in range(100002)]
    li [1], li[2] = False , True
    for i in range(3,int(100002**0.5),2):
        for j in range(i*i,100002,i): li[j] = False
    count = 0
    for i in range(a,b + 1):
        if li[i]: count += 1
    print(count)
if __name__ =="__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        a,b = map(int,input().split())
        prime_numbers(a,b)

"""import math

prime = [True] * 100001
prime[0] = False
prime[1] = False

for i in range(2, math.ceil(math.sqrt(100001))):
    if prime[i] == True:
        j = 2
        while i * j < 100001:
            prime[i * j] = False
            j += 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    for i in range(a, b + 1, 1):
        if prime[i] == True:
            ans += 1
    print(ans)"""

