class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        right_cand = [len(s) for _ in range(len(s))]
        left_cand = [0 for _ in range(len(s))]

        idx = 0
        for i in range(len(s)):
            if s[i] == '|':
                idx = i
            left_cand[i] = idx
        idx = len(s)
        for i in range(len(s) - 1, - 1, - 1):
            if s[i] == '|':
                idx = i
            right_cand[i] = idx
        
        prefix = [0 for _ in range(len(s) + 1)]
        total = 0
        for i, c in enumerate(s):
            if c == '*':
                total += 1
            prefix[i + 1] = total
        
        res = []
        for s, e in queries:
            left_bound = right_cand[s]
            right_bound = left_cand[e]
            if left_bound <= right_bound:
                res.append(prefix[right_bound + 1] - prefix[left_bound])
            else:
                res.append(0)
        return res
            
# time O(n+q)
# space O(n), due to preprocessing lists, not counting output
# using array and prefix sum and standard prefix sum
'''
1. boundary processing
2. prefix sum
'''