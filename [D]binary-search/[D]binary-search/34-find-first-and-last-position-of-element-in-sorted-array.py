class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                boundary = m
                right = m - 1
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        res.append(boundary)

        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                boundary = m
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        res.append(boundary)
        return res
    
# time O(logn)
# space O(1)
# using binary search and search in a sorted array for specific val