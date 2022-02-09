from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        arr1 = Counter(words1)
        arr2 = Counter(words2)
        c = 0
        for i in arr1:
            if arr1[i] == 1 and arr2[i] == 1:
                c+=1
        return c

'''arr1 = Counter(list(map(str,input().split())))
arr2 = Counter(list(map(str,input().split())))
l1 = list()
l2 = list()
count = 0
for i in arr1:
    if arr1[i] == 1:
        l1.append(i)
for i in arr2:
    if arr2[i] == 1:
        l2.append(i)
for i in l1:
    if i in l2:
        count += 1
print(count)'''


'''arr1 = Counter(list(map(str,input().split())))
arr2 = Counter(list(map(str,input().split())))
c = 0
for i in arr1:
    if arr1[i] == 1 and arr2[i] == 1:
        c+=1
print(c)'''
