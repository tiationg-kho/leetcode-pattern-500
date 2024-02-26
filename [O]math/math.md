# math

## intro
- carry
    - in addition, carry is a number that moves to the next column when adding two nums and their column sum is too big for that digit (should consider we are using which base)
- division
    - using division help us constructing a num without converting it to a string
- catalan number
    - Cn = C(2n, n) / (n+1) or (2n)! / (n+1)!n!
        - C0 is the base case, equal to 1
        - Cn is calculated by summing the product of Catalan numbers Ci and Cn-i-1 for all i from 0 to n-1
            - C0 = 1
            - C1 = C0 * C0 = 1
            - C2 = C0 * C1 + C1 * C0 = 2
            - C3 = C0 * C2 + C1 * C1 + C2 * C0 = 5
            - C4 = C0 * C3 + C1 * C2 + C2 * C1 + C3 * C0 = 14
            - C5 = C0 * C4 + C1 * C3 + C2 * C2 + C3 * C1 + C4 * C0 = 42
        - C0 = 1, C(n+1) = Cn * ((4n + 2) / (n + 2))
    - related problem
        - unique BST / unique full binary tree
            - think about choose root node first then decide the left and right child
            - each number 1 through n can be the root, and the number of unique trees is the product of the number of unique trees in the left and right subtrees, which are themselves Catalan Numbers
            - eg. when n = 3 (node 1, 2 ,3)
                - node 1 as root, so 0 node at left, 2 nodes at right
                - node 2 as root, so 1 node at left, 1 node at right
                - node 3 as root, so 2 nodes at left, 0 node at right
        - balanced parentheses
            - think about we got single fixed pair of parentheses
            - we can put x pairs inside it, and y pairs after (at right side of) this fixed pair
            - eg. when n = 3
                - 2 pairs inside, 0 pair right side
                - 1 pairs inside, 1 pair right side
                - 0 pairs inside, 2 pair right side
        - valid stack orderings
            - we can convert this problem into balanced parentheses
- gcd (greatest common divisor) or lcm (least common multiple)
    ```python
    import math

    def get_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def get_gcd_builtin(x, y):
        return math.gcd(x, y)

    def get_lcm(x, y):
        return (x * y) // math.gcd(x, y)
        
    def get_lcm_builtin(x, y):
        return math.lcm(x, y)
    ```

## pattern
- sieve of eratosthenes
    - can get all prime nums in certain range in `O(nloglogn)`
    ```python
    def get_primes(n):
        if n <= 1:
            return []
        primes = [True for _ in range(n + 1)]
        primes[0] = False
        primes[1] = False
        for p in range(2, int((n + 1) ** 0.5) + 1):
            if primes[p]:
                for mul_p in range(p ** 2, n + 1, p):
                    primes[mul_p] = False
        return [i for i, p in enumerate(primes) if p]
    
    # time O(nloglogn)
    # space O(n)
    # using math and sieve of eratosthenes
    ```
- exponentiation by squaring
    - help us impl pow func 
    - defind a recursive func to handle base case, even exponent, odd exponent
    ```python
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
    
    # time O(logn)
    # space O(logn)
    # using math and exponentiation by squaring
    ```
- rejection sampling
    - can generate observations from a distribution that is difficult to sample from directly
    - steps: choose distribution, generate samples, accept or reject, repeat sampling
    ```python
    def rand10():
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1
            
    # time O(1) or O(inf)
    # space O(1)
    # using math and rejection sampling
    '''
    1. (rand7() - 1) * 7, generate 0,7,14,21,28,35,42
    2. after + rand7(), will have random num between 1 - 49 with equal probability
    3. then use rejection sampling, if num not in desired range then re-sample it
    4. if num in desired range, and inside range every num has same probability, then choose it
    '''
    ```
- math

