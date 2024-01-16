class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums = [lower - 1] + nums + [upper + 1]
        res = []
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            cur = nums[i]
            if cur - prev >= 2:
                res.append([prev + 1, cur - 1])
        return res
    
# time O(n)
# space O(n)
# using array and pre-process