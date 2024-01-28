class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[- 1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
    
# time O(n), each temperature will only pop and push once and both cost O(1)
# space O(n), due to stack's size
# using stack and queue and montonic and monotonic stack (consider one side’s relationship)