class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, boundary = 0, len(nums) - 1, len(nums)
        while left <= right:
            m = (left + right) // 2
            if nums[m] >= target:
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary

# time O(logn)
# space O(1)
# using binary search and search in a sorted array for most close val