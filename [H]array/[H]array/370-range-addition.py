class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        diffs = [0 for _ in range(length)]
        for s, e, inc in updates:
            diffs[s] += inc
            if e + 1 < length:
                diffs[e + 1] -= inc
        
        total = 0
        for i, d in enumerate(diffs):
            total += d
            diffs[i] = total
        return diffs
        
# time O(n+k), k is the length of updates
# space O(1), if not counting output list
# using array and difference array