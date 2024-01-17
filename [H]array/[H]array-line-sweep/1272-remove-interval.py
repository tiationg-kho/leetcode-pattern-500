class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        res = []
        prev_s, prev_e = toBeRemoved
        for i, (cur_s, cur_e) in enumerate(intervals):
            if cur_s >= prev_e:
                res.extend(intervals[i:])
                return res
            elif cur_e <= prev_s:
                res.append([cur_s, cur_e])
            else:
                if cur_s < prev_s:
                    res.append([cur_s, prev_s])
                if cur_e > prev_e:
                    res.append([prev_e, cur_e])
        
        return res
    
# time O(n)
# space O(n), due to output list
# using array and line sweep and compare two intervals each round