class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                res[i] = max(res[i], res[i - 1] + 1)
        
        for i in range(n - 2, - 1, - 1):
            if ratings[i + 1] < ratings[i]:
                res[i] = max(res[i], res[i + 1] + 1)
        
        return sum(res)

# time O(n)
# space O(n)
# using greedy
'''
1. make sure to get more than left child if cur child have higher rating
2. make sure to get more than right child if cur child have higher rating
'''