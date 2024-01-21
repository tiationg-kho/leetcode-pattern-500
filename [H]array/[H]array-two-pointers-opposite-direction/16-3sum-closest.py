class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        res_diff = float('inf')
        res = None

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            small_three = nums[i] + nums[left] + nums[left + 1]
            if small_three > target:
                if abs(small_three - target) < res_diff:
                    res_diff = abs(small_three - target)
                    res = small_three
                break
            large_three = nums[i] + nums[right - 1] + nums[right]
            if large_three < target:
                if abs(large_three - target) < res_diff:
                    res_diff = abs(large_three - target)
                    res = large_three
                continue
            
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if abs(cur - target) < res_diff:
                    res_diff = abs(cur - target)
                    res = cur
                if cur == target:
                    return target
                elif cur > target:
                    right -= 1
                else:
                    left += 1
        return res

# time O(n**2)
# space O(1), not count built in sort's cost
# using array and two pointers opposite direction and shrink type and sort and prune