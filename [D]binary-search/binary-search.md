# binary search

## intro

```python
# approach 1
# search in a sorted array for specific val
# or search in sth’s range
class Solution:
    def binary_search(self, nums, TARGET):
        left, right, boundary = 0, len(nums) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] > TARGET:
                right = m - 1
            elif nums[m] == TARGET:
                boundary = m
                break
            else:
                left = m + 1
        return boundary
```

```python
# approach 2
# search in a sorted array for most close val to specific val
# or search in sth’s range
class Solution:
    def binary_search(self, nums, LIMIT):
        left, right, boundary = LOW_BOUND, UP_BOUND, - 1
        
        def valid(PARAMETERS):
            SOME OPS DUE TO LIMIT
            return BOOL
        
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1 # or left = m + 1
            else:
                left = m + 1 # or right = m - 1
        return boundary
```

- an efficient sorted array search algorithm
    - can search for specific val
    - can search for most close val to specific val
    - can make a binary decision to shrink the search range
- time `O(log(n))`, space `O(1)`
- left and right can be a range from
    - sorted array’s start and end
    - sth’s low_bound and up_bound
- use a boundary (ptr) to record the current best/valid answer, then try to get better one

## pattern

**search in a sorted array for specific val**

- when shrinking, will have 3 logic branch mostly

**search in a sorted array for most close val**

- when shrinking, will have 2 logic branch mostly

**search in sth’s range**

- search between sth’s low_bound and up_bound
    - num
    - length
    - capacity
    - distance
    - total
    - sum
- can be for specific val or for most close val. mostly for most close val

**use a boundary to record**

- depends on different condition, binary search could have different logic branch, and inside certain branch could record the boundary
- when recording, we should consider the concept of greedy algorithm
- implement
    - use - 1 to initiation, to handle not find situation
        - inside branch, record most valid answer in cur condition
    - or use len(nums) - 1 to initiation, as a potential valid answer
        - inside branch, record most valid answer in cur condition
    - or doesn’t need it, when it is guaranteed to have a specific answer

**rotated sorted array**

- if we compare mid to right, we could know we are inside the first part (large val part when mid is larger than right) or second part (small val part when mid is smaller than right)
    - then figure out our target val is
        - between left and mid (ascending order)
        - not between left and mid (not sure)
        - between mid and right (ascending order)
        - not between mid and right (not sure)
    - notice: above approach is based on the array only contain unique vals
        - if contain duplicate vals, when the mid == right (means cannot decide we are inside which part), we can only wipe out this one element in this round
- if we use right as initial boundary, we can compare mid to boundary each round to find the min val in array
    - if less than
        - means we are at small part (first round)
        - record it
        - keep search the left side
    - if larger than
        - means we are at large part (first round)
        - keep search the right side