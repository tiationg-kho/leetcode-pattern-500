class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = None
        for i in range(len(nums) - 1, - 1, - 1):
            if i - 1 >= 0 and nums[i - 1] < nums[i]:
                a = i - 1
                break
        if a == None:
            left, right = 0, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return
        
        b = a + 1
        for i in range(len(nums) - 1, a, - 1):
            if nums[a] < nums[i]:
                b = i
                break
        
        nums[a], nums[b] = nums[b], nums[a]

        left, right = a + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# time O(n), worst case traverse all list
# space O(1)
# using array and two pointers same direction and find next permutation
'''
1. find first relative small (left neighbor < cur element) num a in right side (if can not find a, then we are already in the largest permutation)
2. find first relative large num b (to that relative small num a) in right side
3. swap a and b
4. let second half subarray (after that swap idx (b's new idx)) become monotonic increasing (reverse them)
'''