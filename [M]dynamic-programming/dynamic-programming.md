# dynamic programming

## intro

- dp
    - solving bigger problems using smaller problems while saving results to avoid repeated calculations
    - dp problem is about
        - count of ways
        - minimum
        - maximum
    - a problem is a dp problem if it satisfy three conditions
        1. the problem can be divided into subproblems, and its optimal solution can be constructed from optimal solutions of the subproblems (**optimal substructure**)
        2. the subproblems **overlap**
        3. ****no aftereffect****
    - example of problem has optimal substructure but subproblems do not overlap
        - merge sort
            - so we use divide and conquer not dp to solve merge sort
    - dp vs greedy
        -  in dp, we solve overall problem by combining the solutions to subproblems
        -  in greedy, we make a series of localized optimal choices without considering the overall problem
    - two approaches of dp
        - top-down approach (memoization)
            - dfs and cache table
        - bottom-up approach (tabulation)
            - for loop and dp table
    - steps of bottom-up dp
        - define how to divide into smaller subproblems
        - create dp table to store results for these subproblems
        - fill dp table for base cases
        - find out the formula about how to combine subproblems result to larger problem's result
        - start for loop and use formula we just found to fill rest of dp table

## pattern

- 2D
    - use dp[i][j]
    - use a 2D array for memo
- knapsack
    - use dp[i]
    - dp table's size is the volume of the knapsack, and dp[i] is the value of size i knapsack
    - 0-1 knapsack
        - one item can only be selected once
    ```python
    for num in nums:
        for total in range(target, num - 1, - 1):
    ```
    - complete knapsack
        - one item can be selected several times
    ```python
    for num in nums:
        for total in range(1, target + 1):
    ```
    - combination knapsack
        - consider the select ways of item
    ```python
    for num in nums:
        for total in range(1, target + 1):
    ```
    - permutation knapsack
        - consider the select order of item
    ```python
    for total in range(1, target + 1):
        for num in nums:
    ```
- linear sequence
    - use dp[i]
- double sequence
    - use dp[i][j]
- interval (start from one interval)
    - use dp[i][k]
- interval (start from short interval)
    - use dp[i][j]


