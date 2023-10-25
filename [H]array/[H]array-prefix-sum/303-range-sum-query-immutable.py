class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            self.prefix[i + 1] = total

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# time O(1) for sumRange(), O(n) for initiation
# space O(n)
# using array and prefix sum and standard prefix sum