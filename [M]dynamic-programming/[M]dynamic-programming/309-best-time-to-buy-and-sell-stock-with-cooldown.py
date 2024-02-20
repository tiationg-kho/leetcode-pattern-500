class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_hold = 0
        hold = float('-inf')
        cooldown = 0
        for p in prices:
            not_hold, hold, cooldown = max(not_hold, cooldown), max(hold, - p, not_hold - p), max(cooldown, hold + p)
        return max(not_hold, cooldown)

# time O(n)
# space O(1)
# using dynamic programming and linear sequence