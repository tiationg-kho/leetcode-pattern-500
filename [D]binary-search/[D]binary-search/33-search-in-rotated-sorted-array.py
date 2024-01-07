class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                boundary = m
                break
            elif nums[m] > nums[right]:
                if nums[left] <= target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if nums[m] < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1
        return boundary
        
# time O(logn)
# space O(1)
# using binary search and rotated sorted array
'''
1. compare to right ptr
2. if m ptr val larger than right ptr val, means the left side of m ptr has order
3. if m ptr val less than right ptr val, means the right side of m ptr has order
'''