class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], - x[1]))

        res = 0
        prev_s, prev_e = intervals[0]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if prev_e >= cur_e:
                res += 1
            else:
                prev_s, prev_e = cur_s, cur_e

        return len(intervals) - res
        
# time O(nlogn)
# space O(1) or consider the built in sort's cost
# using array and line sweep and compare two intervals each round and sort and greedy