class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        state = 0
        start = 0
        res = 0

        for i in range(1, len(arr)):
            if state == 0:
                if arr[i - 1] < arr[i]:
                    state = 1
                    start = i - 1
            elif state == 1:
                if arr[i - 1] == arr[i]:
                    state = 0
                elif arr[i - 1] > arr[i]:
                    state = 2
                    res = max(res, i - start + 1)
            else:
                if arr[i - 1] < arr[i]:
                    state = 1
                    start = i - 1
                elif arr[i - 1] == arr[i]:
                    state = 0
                else:
                    res = max(res, i - start + 1)
        
        return res

# time O(n)
# space O(1)
# using array and finite state machine
'''
1. state 0 for undefined, 1 for uphill, 2 for downhill
'''