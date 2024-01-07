class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right, boundary = 0, len(nums) - 2, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] > nums[m + 1]:
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary
    
# time O(logn), due to binary search
# space O(1)
# using binary search and use boundary to record