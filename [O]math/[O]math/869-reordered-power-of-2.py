class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        def check(num):
            res = [0 for _ in range(10)]
            while num:
                num, remainder = divmod(num, 10)
                res[remainder] += 1
            return res

        target = check(n)
        val = 1
        for i in range(31):
            if check(val) == target:
                return True
            val <<= 1
        return False
    
# time O(1)
# space O(1)
# using math