class Solution:
    def numOfStrings(self, arr: List[str], word: str) -> int:
        c = 0
        for i in arr:
            if i in word:
                c+=1
        return c

'''arr = list(map(str,input().split()))
w = str(input())
c = 0
for i in arr:
    if i in w:
        c+=1
print(c)'''

