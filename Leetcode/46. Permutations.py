class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r=itertools.permutations(nums,len(nums))
        return r

