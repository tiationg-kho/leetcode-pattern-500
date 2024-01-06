class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def valid(bound):
            total = 0
            day = 1
            for w in weights:
                if w > bound:
                    return False
                if total + w > bound:
                    total = w
                    day += 1
                else:
                    total += w
            return day <= days

        left, right, boundary = 1, sum(weights), - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary

# time O(nlogm), n is the number of weights for the traversion's cost, and m is the sum of weights for binary search's cost
# space O(1)
# using binary search and search in sth’s range