class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        temp = [float('inf')] + nums + [float('inf')]
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[- 1]] < temp[i]:
                idx = stack.pop()
                left_bound = stack[- 1]
                right_bound = i
                res += (idx - left_bound) * (right_bound - idx) * temp[idx]
            stack.append(i)
        temp = [float('-inf')] + nums + [float('-inf')]
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[- 1]] > temp[i]:
                idx = stack.pop()
                left_bound = stack[- 1]
                right_bound = i
                res -= (idx - left_bound) * (right_bound - idx) * temp[idx]
            stack.append(i)
        return res
            
# time O(n), due to traverse twice
# space O(n), due to stack
# using stack and queue and montonic and monotonic stack (consider two side’s relationship)