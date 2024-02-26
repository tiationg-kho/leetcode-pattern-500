class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n < 0:
                return 1 / helper(x, - n)
            if n == 0:
                return 1.0
            if n == 1:
                return x
            half = helper(x, n // 2)
            if n % 2 == 1:
                return x * half * half
            return half * half
        
        return helper(x, n)

# time O(logn), each time divide to half
# space O(logn), due to recursion stack
# using math and exponentiation by squaring