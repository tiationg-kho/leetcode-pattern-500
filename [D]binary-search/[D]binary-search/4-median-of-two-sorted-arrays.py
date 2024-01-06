class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        
        left, right = 0, len(A)
        while left <= right:
            m = (left + right) // 2
            lenA = m
            lenB = total // 2 - lenA
            leftA = A[lenA - 1] if lenA - 1 >= 0 else float('-inf')
            rightA = A[lenA] if lenA < len(A) else float('inf')
            leftB = B[lenB - 1] if lenB - 1 >= 0 else float('-inf')
            rightB = B[lenB] if lenB < len(B) else float('inf')
            if leftA > rightB:
                right = m - 1
            elif leftB > rightA:
                left = m + 1
            else:
                break

        return min(rightA, rightB) if total % 2 else (max(leftA, leftB) + min(rightA, rightB)) / 2

# time O(log(min(m, n))), due to binary search
# space O(1)
# using binary search and search in sth’s range
'''
1. median can divide a sorted array(listA + listB) to two part with same length
2. use binary search to find the length of listA to contribute into the first part of sorted array, 
   will get the length of listB to contribute into the first part of sorted array at the same time
3. then we use these two length to get the cut points inside listA and listB, 
   will get 4 nums before/after the cut points
4. compare them, if the condition is not correct, 
   then keep search the correct length of listA to contribute into the first part of sorted array
5. if condition is correct, just deal with two situation of getting median
'''