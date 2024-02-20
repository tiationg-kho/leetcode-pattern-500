class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = [[0, float('-inf')] for _ in range(3)]

        for p in prices:
            first_buy = max(sell[0][1], - p)
            first_sell = max(sell[1][0], sell[0][1] + p)
            second_buy = max(sell[1][1], sell[1][0] - p)
            second_sell = max(sell[2][0], sell[1][1] + p)
            sell[0][1] = first_buy
            sell[1][0] = first_sell
            sell[1][1] = second_buy
            sell[2][0] = second_sell
        return max(sell[1][0], sell[2][0])
    
# time O(n)
# space O(1)
# using dynamic programming and linear sequence