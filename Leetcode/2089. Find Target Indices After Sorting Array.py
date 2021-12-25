class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        a = []
        for i,j in enumerate(nums):
            if j == target:
                a.append(i)
        return a


'''class solution:
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target
        a = []
        nums.sort()
        for i,j in enumerate(nums):
            if j == target:
                a.append(i)
        print(a)

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    target = int(input())
    solution(nums,target)'''

