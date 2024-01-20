class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return left
    
# time O(n)
# space O(1)
# using array and two pointers same direction and left ptr to record