class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        cur = 0
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
                
# time O(n)
# space O(1)
# using array and two pointers same direction and left ptr to record
'''
1. when swap with left ptr, cur ptr with only get 1 or 0
2. most time is 1. And 0 is when cur ptr swap with left ptr at same idx
3. so cur need plus 1
'''