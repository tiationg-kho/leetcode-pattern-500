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
        - compare cur element with stack[- 1] element then decide next steps accordingly
    
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
    - notice when to store/peek/modify last states
- **implement stack/queue**
    - queue by stack
        - two stacks
            - use reverse technique to place elements
            - enqueue: push elements into stack1
            - dequeue: when needed, reverse the order by moving all elements from stack1 to stack2, so the first/oldest element enqueued is now on top of stack2 and will be popped off
            - push is `O(1)`, pop is `amortized O(1)`
    - stack by queue
        - only one queue
            - visualize queue as circular, move all older elements (ahead of new added element) to new added element's tail, ensuring the new added element is always at the front of queue to simulate the stack
            - push is `O(n)`, pop is `O(1)`
    - min stack (push, pop, peek, get_min)
        - only one stack
            - the stack must store the diff val between cur val and cur min_num
            - push is `O(1)`, pop is `O(1)`, peek is `O(1)`, get_min is `O(1)`
    - max stack (push, pop, peek, get_max, pop_max)
        - stack and heap and hashmap
            - assist with lazy removal technique
            - push is `O(logn)`, pop is `amortized O(logn)`, peek is `O(1)`, get_max is `O(1)`, pop_max is `amortized O(logn)`
    - max freq stack (push, pop_mostfreq)
        - stack and hashmap
            - use val as key, to count the frequency
            - use freq as key, to access the stack of that freq
- **use variables to simulate stack**
    - when the types of elements in stack are limited
    - often use for validating parentheses, and need to use a greedy approach to find longest
        - traverse from start once
        - then traverse back again
- **use stack to simulate**
    - can simulate text editor
        - user two stack or dll
    - can simulate nested list iterator
- **use monotonic queue and sliding window**
    - if we want to maintain the min/max value and there is a constraint/consideration about the length of valid subarray (sliding window)
        - eg. get every [i, i + k - 1] subarray's min/max value
            - naive way might take O(nk)
            - use monotonic queue only spend O(n)
                - the min/max will be located at queue' head
    - notice
        - when to pop element at queue’s end
        - when to add element at queue’s end
        - when the element at queue’s start is expired
        - when to record the cur best res
        - (order of these steps is not guaranteed)
- **use monotonic stack (consider one or two side’s relationship)**
    - notice
        - when to pop element at stack's end
        - when to add element at stack’s end
    - monotonic increasing or decreasing array will be generated
    - there’s two type of this technique
        - consider one side’s relationship
        - consider two side’s relationship
    - can find out the left and/or right bound for each element in some condition
        - finding the left and/or right relative smaller/larger elements for each element
        - finding the smallest/largest element in every subarray
    - can use sentinel element at left bound or/and right bound
        - help us to handle edge case