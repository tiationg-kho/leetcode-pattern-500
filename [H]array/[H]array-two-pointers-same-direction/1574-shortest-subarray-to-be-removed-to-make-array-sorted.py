class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = None
        for i in range(len(arr)):
            if i - 1 >= 0 and arr[i - 1] > arr[i]:
                left = i - 1
                break
        right = None
        for i in range(len(arr) - 1, - 1, - 1):
            if i + 1 < len(arr) and arr[i] > arr[i + 1]:
                right = i + 1
                break
        if left == None:
            return 0

        res = min(right, len(arr) - (left + 1))
        
        p1, p2 = 0, right
        while p1 < left + 1 and p2 < len(arr):
            if arr[p1] <= arr[p2]:
                res = min(res, p2 - p1 - 1)
                p1 += 1
            else:
                p2 += 1
        return res
        
# time O(n)
# space O(1)
# using array and two pointers same direction and traverse two sequences
'''
1. find valid left subarray
2. find valid right subarray
3. record res: discard whole rest array of valid left subarray or whole rest array of valid right subarray
4-1. start from discard whole rest array of valid right subarray
4-2. consider restore one element at leftest side, this might make us to discard some elements in origin valid right subarray
4-3. keep trying to restore elements
'''