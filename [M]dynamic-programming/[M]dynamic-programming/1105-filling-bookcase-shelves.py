class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [float('inf') for _ in range(len(books) + 1)]
        dp[0] = 0

        for i in range(1, len(books) + 1):
            cur_width, cur_height = 0, 0
            for j in range(i - 1, - 1, - 1):
                cur_width += books[j][0]
                cur_height = max(cur_height, books[j][1])
                if cur_width > shelfWidth:
                    break
                dp[i] = min(dp[i], cur_height + dp[j])
        
        return dp[len(books)]
    
# time O(n**2)
# space O(n)
# using dynamic programming and linear sequence