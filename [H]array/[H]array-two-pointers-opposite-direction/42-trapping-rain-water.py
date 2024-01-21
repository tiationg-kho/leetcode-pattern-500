class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        left_wall, right_wall = height[left], height[right]
        while left < right:
            left_wall = max(left_wall, height[left])
            right_wall = max(right_wall, height[right])
            if left_wall < right_wall:
                res += left_wall - height[left]
                left += 1
            else:
                res += right_wall - height[right]
                right -= 1
        return res
        
# tiem O(n), due to traverse
# space O(1)
# using array and two pointers opposite direction and shrink type and greedy
'''
1. count the water with lower wall's side first
'''