# stack and queue

## intro

- **stack**
    - last in, first out
    - recursion and function calls are implemented with stack behind the scene
    - implementation
        - array
        - top pointer
            - pointing to the top of the stack (usually the next unused space)
        - when inserting an item, we set the value at the pointer to the item and increment the pointer by 1
        - when removing an item, we decrease the pointer by 1
    - tips
        - compare cur element with stack[- 1] element then decide next move accordingly
    
    ```python
    # init the stack
    stack = []
    
    # push 5 into the stack, O(1)
    stack.append(5)
    
    # peek top/newest item, O(1)
    print(stack[- 1]) # 5
    
    # pop out the top item, O(1)
    val = stack.pop() # 5
    
    # get length, O(1)
    len(stack) # 0
    ```

- **queue**
    - first in, first out
    - bfs use queue
    - implementation
        - array
            - to save place, we make array circular
        - start pointer
            - pointing to the start of the queue
        - end pointer
            - pointing at the end of the queue
        - when inserting an item into the queue, we set the entry at the end pointer to the value and increase the end pointer by 1
        - when removing an item from the queue, we increase the start pointer by 1
    - tipes
        - deque is a double-ended queue
    
    ```python
    from collections import deque
    
    # init
    q = deque([])
    
    # add at the end, O(1)
    q.append(5) # q is deque([5])
    q.append(100) # q is deque([5, 100])
    
    # peek the first/oldest element, O(1)
    q[0] # 5
    
    # get length, O(1)
    len(q) # 2
    
    # remove from the front, O(1)
    q.popleft() # 5, q become deque([100])
    ```

- **monotonic stack and monotonic queue**
    - store idx or val (most of times store idx)
    - monotonic increasing or decreasing
    - during for loop, compare cur element with queue[-1]/stack[- 1] element
        - then pop the invalid element

## pattern

- **use queue to simulate**
    - can simulate data stream
- **use stack to store the last states**
    - notice when to store and when to check to last states
- **implement stack/queue**
    - queue by stack
        - two stacks
            - use reverse technique to place elements
    - stack by queue
        - only one queue
            - place old elements from new elements left side to new element’s right side
    - min stack
        - only one stack
            - the stack must store the diff between cur val and min_num
    - max stack
        - stack and heap and hashmap
            - assist with lazy removal technique
    - max freq stack
        - stack and hashmap
            - use freq as key, to access the stack of that freq
- **use variables to simulate stack**
    - when the types of elements in stack are limited
    - often use for validating parentheses, and need to use a greedy approach to find longest
        - traverse from start once
        - then traverse back again
- **use stack to simulate**
    - can simulate text editor
        - user two stack or dll
    - can simulate iterator
- **use monotonic queue and sliding window**
    - if we want to maintain the min/max value and there is a constraint about the length of valid subarray(sliding window)
    - notice
        - when to pop element at queue’s end
        - when to add element at queue’s end
        - when the element at queue’s start is expired
    - steps (can reorder or combine)
        1. update states due to right ptr is moving
            - using monotonic queue
        2. move left ptr to maintain valid
            - update states due to left ptr is moving
                - using monotonic queue
        3. if valid
            - record cur best res
- **use monotonic stack (consider one or two side’s relationship)**
    - notice
        - when to pop element at stack end
        - when to add element at stack’s end
    - monotonic increasing or decreasing array will be initialized
    - there’s two type of this technique
        - consider one side’s relationship
        - consider two side’s relationship
    - can find out the left and/or right bound for each element in some condition
        - finding the left and/or right relative smaller/larger elements for each element
        - finding the smallest/largest element in every subarray
    - can use sentinel element at left bound or/and right bound
        - help us to handle edge case