from collections import defaultdict
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        peaks.sort()
        stack = []
        for i in range(len(peaks)):
            x, y = peaks[i]
            while stack and stack[- 1][1] <= y - (x - stack[- 1][0]):
                stack.pop()
            if not stack or (stack[- 1][1] - (x - stack[- 1][0]) < y):
                stack.append((x, y))

        peak_count = defaultdict(int)
        for x, y in peaks:
            peak_count[(x, y)] += 1
        same_peak = 0
        for p in stack:
            if peak_count[p] > 1:
                same_peak += 1
            
        return len(stack) - same_peak
    
# time O(nlogn)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider one side’s relationship) and hashmap and sort