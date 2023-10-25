# dynamic programming

## intro

- dp
    - solving bigger problems using smaller problems while saving results to avoid repeated calculations
    - dp problem is about
        - shortest
        - longest
        - minimum
        - maximum
        - ways
    - a problem is a dp problem if it satisfy three conditions
        1. The problem can be divided into subproblems, and its optimal solution can be constructed from optimal solutions of the subproblems (**optimal substructure**)
        2. The subproblems **overlap**
        3. ****No aftereffect****
    - example of problem has optimal substructure but subproblems do not overlap
        - merge sort
            - so we use divide and conquer not dp to solve merge sort
    - two approaches
        - top-down approach (memoization)
            - dfs and cache table
        - bottom-up approach (tabulation)
            - for loop and dp table
- 0-1 knapsack
    - one item only be selected once

```python
for num in nums:
    for total in range(target, nums - 1, - 1):
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

## pattern

- time sequence
    - use dp[i]
- double sequence
    - use dp[i][j]
- interval (start from one interval)
    - use dp[i][k]
- interval (start from short interval)
    - use dp[i][j]
- knapsack
- 2D
