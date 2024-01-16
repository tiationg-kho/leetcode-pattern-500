class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        p1, p2 = 0, slow
        while True:
            p1 = nums[p1]
            p2 = nums[p2]
            if p1 == p2:
                break
        
        return p1
            
# time O(n)
# space O(1)
# using array and specific range array (cycle detection)
'''
1. (L + P ) * 2 = L + P + Q + P
2. L = Q
'''