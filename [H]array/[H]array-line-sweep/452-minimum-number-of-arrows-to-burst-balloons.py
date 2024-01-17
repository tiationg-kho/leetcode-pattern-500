class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        res = 0
        prev_e = points[0][1]
        for i in range(1, len(points)):
            cur_s, cur_e = points[i]
            if prev_e < cur_s:
                res += 1
                prev_e = cur_e
            else:
                prev_e = min(prev_e, cur_e)
            
        res += 1

        return res
    
# time O(nlogn)
# space O(1), not counting built in sort cost
# using array and line sweep and compare two intervals each round and sort and greedy
'''
1. only end ptr matters
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: x[1])

        res = 0
        prev_e = points[0][1]
        for i in range(1, len(points)):
            cur_s, cur_e = points[i]
            if prev_e < cur_s:
                res += 1
                prev_e = cur_e
            
        res += 1

        return res

# time O(nlogn)
# space O(1), not counting built in sort cost
# using array and line sweep and compare two intervals each round and sort and greedy
'''
1. only end ptr matters
'''