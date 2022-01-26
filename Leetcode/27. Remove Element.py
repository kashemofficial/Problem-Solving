class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


'''n = list(map(int,input().split()))
val = int(input())
i,j = 0,0
while j < len(n):
    if n[j] != val:
        n[i] = n[j]
        i+=1
    j+=1
print(i)'''