class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])

        res = 0
        prev_s, prev_e = intervals[0][1] - 1, intervals[0][1]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if prev_e < cur_s:
                res += 2
                prev_s, prev_e = cur_e - 1, cur_e
            elif prev_s < cur_s:
                res += 1
                if prev_e != cur_e:
                    prev_s, prev_e = prev_e, cur_e
                else:
                    prev_s, prev_e = cur_e - 1, cur_e
                
        res += 2
            
        return res

# time O(nlogn)
# space O(1), or due to built in sort's cost
# using array and line sweep and compare two intervals each round and sort and greedy
'''
1. sort by end, so we can handle early end's interval first
2-1. greedly choose last two number because they get better chance to overlap with others
2-2. if we are not sorting by end, then we cannot decide how to choose the best two number
3-1. totally miss
3-2-1. only cover one number (one num remain, one num is new interval end)
3-2-2. only cover one number (one num remain, but collision with new interval end)
'''