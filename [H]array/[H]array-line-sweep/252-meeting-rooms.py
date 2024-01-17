class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort()

        prev_s, prev_e = intervals[0]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if prev_e <= cur_s:
                prev_s, prev_e = cur_s, cur_e
                continue
            return False

        return True

# time O(nlogn)
# space O(1), or consider sort's cost
# using array and line sweep and compare two intervals each round