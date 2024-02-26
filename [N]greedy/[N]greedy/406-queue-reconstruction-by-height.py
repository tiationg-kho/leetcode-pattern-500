class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (- x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
        
# time O(n**2)
# space O(n)
# using greedy and sort
'''
1. sort
2. reconstruct by inserting
'''