class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                if boundary == - 1 or nums[m] < nums[boundary]:
                    boundary = m
                right = m - 1
        return nums[boundary]

# time O(logn)
# space O(1)
# using binary search and rotated sorted array