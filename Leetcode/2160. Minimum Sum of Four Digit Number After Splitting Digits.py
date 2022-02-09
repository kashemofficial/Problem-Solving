class Solution:
    def minimumSum(self, num: int) -> int:
        n = list(str(num))
        n.sort()
        result = int(n[0]+n[3])+int(n[1]+n[2])
        return result


'''num = int(input())
n = list(str(num))
n.sort()
result = int(n[0]+n[3])+int(n[1]+n[2])
print(result)'''


