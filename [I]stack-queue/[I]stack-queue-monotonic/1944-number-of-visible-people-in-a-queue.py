class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(heights))]
        for i in range(len(heights) - 1, - 1, - 1):
            while stack and heights[stack[- 1]] <= heights[i]:
                stack.pop()
                res[i] += 1
            if stack:
                res[i] += 1
            stack.append(i)
        return res

# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider one side’s relationship)
'''
1. person can see people in right (monotonic increasing height)
'''