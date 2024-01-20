class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = float('inf')
        total = 0
        left = 0
        for right in range(len(cardPoints)):
            total += cardPoints[right]
            while right - left + 1 > len(cardPoints) - k:
                total -= cardPoints[left]
                left += 1
            if right - left + 1 == len(cardPoints) - k:
                res = min(res, total)
        return sum(cardPoints) - res

# time O(n)
# space O(1)
# using array and standard sliding window and hashmap