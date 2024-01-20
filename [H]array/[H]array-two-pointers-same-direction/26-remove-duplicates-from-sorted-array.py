class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if left - 1 >= 0 and nums[right] == nums[left - 1]:
                continue
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        return left

# time O(n), due to traverse
# space O(1)
# using array and two pointers same direction and left ptr to record