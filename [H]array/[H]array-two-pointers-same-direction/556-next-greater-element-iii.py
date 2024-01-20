class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        
        a = None
        for i in range(len(nums) - 1, - 1, - 1):
            if i - 1 >= 0 and nums[i - 1] < nums[i]:
                a = i - 1
                break
        if a == None:
            return - 1
        
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
        res = 0
        max_num = 2**31 - 1
        for num in nums:
            if res > max_num // 10 or (res == max_num // 10 and int(num) > max_num % 10):
                return - 1
            res *= 10
            res += int(num)
        return res

# time O(n)
# space O(n)
# using array and two pointers same direction and find next permutation