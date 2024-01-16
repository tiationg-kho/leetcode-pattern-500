class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            while 1 <= nums[i] <= len(nums):
                target_idx = nums[i] - 1
                if nums[i] == nums[target_idx]:
                    break
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1
        
# time O(n)
# space O(1)
# using array and specific range array (cyclic sort)
'''
1. we want to restore array like below
idx:
    0, 1, 2, 3 ..., n-1
val:
    1, 2, 3, 4 ..., n 
2. then we can find out the missing val 
'''