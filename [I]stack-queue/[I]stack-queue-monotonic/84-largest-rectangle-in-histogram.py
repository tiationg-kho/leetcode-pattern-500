class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        res = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[- 1]] > heights[i]:
                idx = stack.pop()
                height = heights[idx]
                left_bound = stack[- 1]
                right_bound = i
                width = right_bound - left_bound - 1
                res = max(res, height * width)
            stack.append(i)
        return res
        
# time O(n)
# space O(n), due to stack
# using stack and queue and montonic and monotonic stack (consider two side’s relationship)
'''
1. decide height
2. then find the left smaller element and right smaller element
3. count the area between these two bound
'''