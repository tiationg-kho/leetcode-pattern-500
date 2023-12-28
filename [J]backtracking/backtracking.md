# backtracking

## intro

- backtracking like dfs on a tree
- if a problem need try and error (make decisions) to enum every res, then use backtracking
    - making decisions
        - each round we got multi choices (must pick one)
        - each round we choose sth or not choose
    - notice elements are duplicate or not
        - if so, we need to take care of pruning
    - notice elements can be chosen repeatedly or not
        - if not, we need to maintain a memo
    - notice that inside backtracking, we can use the boolean value as a return value to indicate whether there is a valid answer or not

```python

def backtrack(res, path, count, memo, index/node):
    if BOUND_REACHED:	
        return

    if GOAL_REACHED:
        res.append(COPIED_PATH)
        return

    for CHOCIE in CHOICES:
        if CHOICE is VALID:
            MAKE_CHOICE
            backtrack(res, path, count, memo, index/node)
            UNDO_CHOICE
```

## pattern

- subset
    - a subset is composed of none or some or all elements from a set
- permutation
    - a permutation is an ordered selection of a certain number of elements from a set
- combination
    - a combination is an unordered selection of a certain number of elements from a set
- backtracking with constraints
    - make choices and backtrack based on certain constraints or conditions
