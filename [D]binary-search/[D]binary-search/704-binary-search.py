class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                boundary = m
                break
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return boundary
    
# time O(logn), n is the length of nums
# space O(1)
# using binary search and search in a sorted array for specific val