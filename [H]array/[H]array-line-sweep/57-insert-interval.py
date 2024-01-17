class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        prev_s, prev_e = newInterval
        for i, (cur_s, cur_e) in enumerate(intervals):
            if prev_e < cur_s:
                res.append([prev_s, prev_e])
                res.extend(intervals[i:])
                return res
            elif prev_s > cur_e:
                res.append([cur_s, cur_e])
            else:
                prev_s, prev_e = min(prev_s, cur_s), max(prev_e, cur_e)

        res.append([prev_s, prev_e])

        return res

# time O(n)
# space O(n), due to output list
# using array and line sweep and compare two intervals each round