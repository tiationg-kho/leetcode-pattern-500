class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right, boundary = 0, len(letters) - 1, 0
        while left <= right:
            m = (left + right) // 2
            if letters[m] > target:
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return letters[boundary]

# time O(logn), due to binary search
# space O(1)
# using binary search and search in a sorted array for most close val