class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def helper(heights):
            heights = [0] + heights + [0]
            stack = []
            res = 0
            for i in range(len(heights)):
                while stack and heights[stack[- 1]] > heights[i]:
                    idx = stack.pop()
                    res = max(res, heights[idx] * (i - stack[- 1] - 1))
                stack.append(i)
            return res

        res = 0
        rows, cols = len(matrix), len(matrix[0])
        prefix = [0 for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    prefix[c] += 1
                else:
                    prefix[c] = 0
            res = max(res, helper(prefix))
        return res
    
# time O(RC)
# space O(C)
# using stack and queue and montonic and monotonic stack (consider two side’s relationship) and prefix