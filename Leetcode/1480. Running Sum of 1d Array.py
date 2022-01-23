class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c = 0
        r = []
        for i in nums:
            c += i
            r.append(c)
        return r

