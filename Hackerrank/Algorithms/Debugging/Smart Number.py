import math
for _ in range(int(input())):
    n = int(input())
    val = int(math.sqrt(n))
    if n/(val*val) == 1:
        print('YES')
    else:
        print('NO')

'''import math
def smart_number(num):
    val = int(math.sqrt(num))
    if num / (val*val) == 1:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")'''

