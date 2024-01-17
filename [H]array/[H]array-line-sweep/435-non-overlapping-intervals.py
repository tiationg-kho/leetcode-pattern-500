class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        res = 0
        prev_s, prev_e = intervals[0]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if prev_e <= cur_s:
                prev_s, prev_e = cur_s, cur_e
            else:
                if cur_e < prev_e:
                    prev_s, prev_e = cur_s, cur_e
                res += 1
        
        return res

# time O(nlogn)
# space O(1), or due to built in sort's cost
# using array and line sweep and compare two intervals each round and sort and greedy