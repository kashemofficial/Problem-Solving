class Solution:
    def checkString(self, n: str) -> bool:
        for i in range(1,len(n)):
            if n[i-1] == 'b' and n[i] == 'a':
                return False
                break
        else:
            return True

'''n = str(input())
for i in range(1,len(n)):
    if n[i-1] == 'b' and n[i] == 'a':
        print(False)
        break
else:
    print(True)'''
