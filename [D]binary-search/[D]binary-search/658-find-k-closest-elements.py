class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left, right, boundary = 0, len(arr) - k - 1, len(arr) - k
        while left <= right:
            m = (left + right) // 2
            if arr[m] > x:
                boundary = m
                right = m - 1
            elif arr[m + k] < x:
                left = m + 1
            elif abs(arr[m] - x) <= abs(arr[m + k] - x):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return arr[boundary: boundary + k]

# time O(log(n - k) + k)
# space O(1), not counting output
# using binary search and use boundary to record
'''
1. make sure to record the rightest choice as first potential res
2. use binary search to find left bound of subarray which is k length
3. if 'mid' is a better choice, then record it and shrink the search range
   (if any choice is better than 'mid', then we can not record it)

4. there are 3 scenarios:

x O O O O O O O O O O  
   [our subarray]      (x is in our left side)

O O O O O O O O O O x  
   [our subarray]      (x is in our right side)

O O O O O x O O O O O
   [our subarray]      (x is inside our subarray)

5. how to decide:

 X                     (x = 5)
[5, 15, 20, 22, 23, 50]
            E   E   E  (begin)
    m   E   E          (1st branch, record it, then keep find LEFT side)

                    X  (x = 50)
[5, 15, 20, 22, 23, 50]
            E   E   E  (begin)
    m   E   E          (2nd branch)
    O   O   O            (choice 1)
        O   O   O        (choice 2 won, so go find RIGHT side)

        X              (x = 20)
[5, 15, 20, 22, 23, 50]
            E   E   E  (begin)
    m   E   E          (3rd branch)
    O   O   O            (choice 1 won, record it, then keep find LEFT side)
        O   O   O        (choice 2)

            X          (x = 22)
[5, 15, 20, 22, 23, 50]
            E   E   E  (begin)
    m   E   E          (3rd branch)
    O   O   O            (choice 1)
        O   O   O        (choice 2 won, so go to 4th branch (go find RIGHT side))
'''