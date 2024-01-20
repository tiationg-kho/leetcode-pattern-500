class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = [None, 0]
        left = 0
        for right in range(len(nums)):
            if cur[0] == None or cur[0] != nums[right]:
                cur[0] = nums[right]
                cur[1] = 1
            elif cur[0] == nums[right] and cur[1] == 1:
                cur[1] = 2
            else:
                continue
            
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        
        return left
    
# time O(n)
# space O(1)
# using array and two pointers same direction and left ptr to record