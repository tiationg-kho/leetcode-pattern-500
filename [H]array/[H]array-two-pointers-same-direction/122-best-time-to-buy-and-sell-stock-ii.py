class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] > prices[left]:
                res += prices[right] - prices[left]
                left = right
            else:
                left = right
        return res
        
# time O(n)
# space O(1)
# using array and two pointers same direction and left ptr to record and greedy