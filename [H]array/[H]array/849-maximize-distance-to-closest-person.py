class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        res = 0
        zero = 0
        edge_zero = False

        for i, s in enumerate(seats):
            if s == 0:
                zero += 1
                if i == 0 or i == len(seats) - 1:
                    edge_zero = True
                if edge_zero:
                    res = max(res, zero)
                else:
                    res = max(res, (zero + 1) // 2)
            else:
                zero = 0
                edge_zero = False
        
        return res
    
# time O(n)
# space O(1)
# using array and count continuous elements