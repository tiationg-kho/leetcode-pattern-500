from heapq import *
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])

        heap = []
        cur_day = 0
        for duration, lastday in courses:
            if cur_day + duration <= lastday:
                heappush(heap, - duration)
                cur_day += duration
            elif heap and - heap[0] > duration:
                cur_day -= - (heappop(heap))
                heappush(heap, - duration)
                cur_day += duration

        return len(heap)
        
# time O(nlogn)
# space O(n)
# using heap and storing and popping out elements and sort and greedy
'''
1. greedy strategy
2. we consider the course with earilier deadline first
3. if we can take, we push in heap
4. if we can not take, we should check any prev course can be replaced or not
5. if so, we pop out that course with longest time, then take cur course (cur course is better choice)
6. if not, we discard cur course
'''