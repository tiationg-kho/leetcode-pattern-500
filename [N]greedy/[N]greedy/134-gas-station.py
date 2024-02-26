class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return - 1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start
    
# time O(n)
# space O(1)
# using greedy
'''
1. check it is possible or not
2. traverse and rule out the impossible start stations
'''