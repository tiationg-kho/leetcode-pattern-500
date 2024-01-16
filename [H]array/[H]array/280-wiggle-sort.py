class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if i % 2 == 0:
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                else:
                    if nums[i] < nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]

# time O(n)
# space O(1)
# using array and swap
'''
1. swap won't affect the relationship of nums[i - 1] and nums[i]
'''