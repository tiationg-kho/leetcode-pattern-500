# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i
        for i in range(n):
            if i == cand:
                continue
            if not knows(i, cand) or knows(cand, i):
                return - 1
        return cand
        
# time O(n), due to traverse twice
# space O(1)
# using greedy