class Solution:
    def search(self, nums: List[int], target: int) -> bool:
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
            elif nums[m] < nums[right]:
                if nums[m] < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1
            else:
                right -= 1
        return True if boundary != - 1 else False

# time O(n), best case O(logn)
# space O(1)
# using binary search and rotated sorted array
'''
1. if we cannot decide which side could be sorted, we can only wipe out one element
2. think about [1,1,1,2,1]
'''