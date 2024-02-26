class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [True for _ in range(n)]
        primes[0] = False
        primes[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if primes[p]:
                for mul_p in range(p ** 2, n, p):
                    primes[mul_p] = False
        return sum(primes)
    
# time O(nloglogn)
# space O(n)
# using math and sieve of eratosthenes