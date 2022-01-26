class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

'''
s = list(map(int,input().split()))
c = []
for i in s:
    c.append(i)
print(len(c[-1]))'''


