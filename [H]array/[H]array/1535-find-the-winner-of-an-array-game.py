class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        
        cur = None
        count = 0
        for i, num in enumerate(arr):
            if num == max_num:
                cur = num
                break
            if not cur:
                cur = num
            elif cur < num:
                cur = num
                count = 1
            else:
                count += 1
            if count == k:
                break
        return cur
                
# time O(n)
# space O(1)
# using array and simulation
'''
1. we can use queue to simulate the game
2. but actually if we met max num, max num will always be res
3. so, we do not need to consider element behind max num (involves the elements which were moved to end)
'''