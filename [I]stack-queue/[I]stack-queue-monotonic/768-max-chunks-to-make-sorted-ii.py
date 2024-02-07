class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            chunk_max = num
            while stack and stack[- 1] > num:
                chunk_max = max(chunk_max, stack.pop())
            stack.append(chunk_max)
        return len(stack)
    
# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider one side’s relationship)
'''
1. [0, 0, 3, 5, 4, 2]
2. [0] [0] [2, 3, 4, 5]
3. we should maintain each chunk's max in stack
'''