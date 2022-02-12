class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = int(num ** (1 / 2))
        if n ** 2 == num:
            return True
        else:
            return False

'''num = int(input())
n = int(num ** (1 / 2))
if n ** 2 == num:
    print(True)
else:
    print(False)'''

