class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left] * (right - left))
                left += 1
            else:
                res = max(res, height[right] * (right - left))
                right -= 1
        return res
    
# time O(n)
# space O(1)
# using array and two pointers opposite direction and shrink type and greedy