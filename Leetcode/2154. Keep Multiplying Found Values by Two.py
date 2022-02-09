class Solution:
    def findFinalValue(self, arr: List[int], n: int) -> int:
        for i in sorted(arr):
            if n == i:
                n*=2
        return n

'''arr = list(map(int,input().split()))
n = int(input())
for i in sorted(arr):
    if n == i:
        n *= 2
print(n)'''


