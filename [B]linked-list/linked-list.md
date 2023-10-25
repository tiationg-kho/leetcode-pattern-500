# linked list

## intro

- sequential access
- linked list doesn’t have index, but can simulate by counting total number of nodes
- in memory, all the nodes spread every where
- we can use linked list to implement queue/deque
- complexity (for singly-linked list)
    - search
        - `O(n)`
    - add/delete at head
        - `O(1)`
    - add/delete at middle, add/delete at tail
        - `O(1)` for add/delete + `O(n)` for search
- implement linked list
    
    ```python
    # definition for singly-linked list
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    ```
    
## pattern

**use sentinel node**

- to link the head node, avoid the head lost after modification
- as a merge point to build new list

```python
dummy = ListNode()
```

**use two pointers**

slow and fast

- detect cycle
    
    ```python
    if not head or not head.next:
        return False
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    ```
    
- find cycle start
    
    ```python
    # 1. (L + P ) * 2 = L + P + Q + P
    # 2. L = Q

    if not head or not head.next:
        return None
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p1, p2 = head, slow
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
    return None
    ```
    
- find middle node
    
    ```python
    # if total length is odd, both work
    # if total length is even, then
    
    # return the first middle node
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
    # return the second middle node
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    ```
    

prev and cur

- reverse list
    
    ```python
    # version 1
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
    
    # version 2
    def reverse_nodes(self, prev_nodes, old_head, old_tail, next_nodes):
        prev = prev_nodes
        cur = old_head
        while cur and cur != next_nodes:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        new_head = prev
        new_tail = old_head
        prev_nodes.next = new_head
        new_tail.next = next_nodes
        return new_tail, next_nodes
    ```
    
- swap nodes in pairs
    
    ```python
    dummy = prev = ListNode(next=head)
    cur = head
    while cur and cur.next:
        prev_nodes = prev
        old_first = cur
        old_second = cur.next
        next_nodes = cur.next.next
        
        prev_nodes.next = old_second
        old_second.next = old_first
        old_first.next = next_nodes
        
        prev = old_first
        cur = next_nodes
    
    return dummy.next
    ```
    
- remove certain nodes
    
    ```python
    dummy = prev = ListNode(next=head)
    cur = head
    while cur:
        if SOME_CONDITION:
            prev.next = None
            cur = cur.next
        else:
            prev.next = cur
            prev = cur
            cur = cur.next
    return dummy.next
    ```
    

find LCA/intersection

- if has LCA/intersection
    - x + p + y = y + p + x
- else
    - x + y = y + x
    - two pointers will became None at the same time
- ```python
  p1, p2 = headA, headB
  while p1 != p2:
      if not p1:
          p1 = headB
      else:
          p1 = p1.next
      if not p2:
          p2 = headA
      else:
          p2 = p2.next
  return p1
  ```

utilize symmetry property
- sometimes, a linked list can have a symmetry property like palindrome. but linked list is one way, we cannot get both end at the same time. we need to:
  - first, find the middle point
  - second, reverse one of two parts
  - third, do the ops one by one for both parts

**get linked list length**

- can stimulate idx

```python
n = 0
cur = head
while cur:
    n += 1
    cur = cur.next
return n
```

**use merge sort to sort list**

- `O(nlogn)` time and `O(1)` space, due to iterative
    
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode(next=head)
        interval_len = 1
        while interval_len < count:
            new_list = dummy
            cur = dummy.next
            while cur:
                interval1_len = 0
                interval1 = cur
                while cur and interval1_len < interval_len:
                    interval1_len += 1
                    cur = cur.next
                interval2_len = 0
                interval2 = cur
                while cur and interval2_len < interval_len:
                    interval2_len += 1
                    cur = cur.next
                while interval1_len or interval2_len:
                    if (interval1_len and interval2_len and interval1.val < interval2.val) or (interval2_len == 0):
                        new_list.next = interval1
                        new_list = new_list.next
                        interval1 = interval1.next
                        interval1_len -= 1
                    else:
                        new_list.next = interval2
                        new_list = new_list.next
                        interval2 = interval2.next
                        interval2_len -= 1
            new_list.next = None
            interval_len *= 2
        return dummy.next

  # time O(nlogn), due to merge sort
  # space O(1)
  # using iterative merge sort (bottom up)
  ```
    
**interweaving nodes**

- create new node and place it next to its original node
- after operations, need to unweave the old nodes and new nodes

**use dll and hashmap together**

- dll allow us to maintain a order (time based)
    - dll can traverse forward and backward
    - add/delete in `O(1)` (head or tail)
    - if combine with hashmap to get node, then add/delete in any place in dll is `O(1)`
```Python
class Dll:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # common methods:
    # append(node)
    # popleft()
    # remove(node)
    # update(node)
    # is_empty()
    # append_left(node)
    # append_before(old_node, new_node)
    # append_after(old_node, new_node)
    # get_first_node()
    # get_last_node()
   
```
- hashmap allow us to search/add/delete in `O(1)`
    - combine with one dll (LRU)
        - maintain capacity
        - maintain a key_node hashmap to quickly get correct node
        - maintain dll
    - combline with multiple dlls (LFU)
        - maintain capacity
        - maintain a key_node hashmap to quickly get correct node
        - maintain min_freq variable
        - maintain a freq_dll hashmap to quickly get the dll of nodes with certain freq


**change val as change node**

- help us to skip certain node without knowing the list’s head

**skiplist**

- `O(logn)` for search/add/delete on average, `O(n)` for worst
- space `O(n)` on average, `O(nlogn)` for worst
    - cause logn layers
- multiple layers linked list
    - each layer has sorted order
    - base layer has every nodes
- search
    - if not in this layer, then go down 1 layer til base level
- add
    - record every potential prev_node (every level)
    - building starts from base level
        - base level must build
        - 50% to continue building
        - if still valid for building, but reach the top level, then construct a new top level by initing a new root node
- delete
    - record every prev_node whose next_node need to be deleted
        - always record the first valid prev_node we met
    - delete these prev_nodes’ next_nodes
    - if we reach base level, but still cannot find any valid prev_node, meaning we cannot delete any node

```python
import random

class ListNode:
    def __init__(self, val=None, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

class Skiplist:

    def __init__(self):
        self.root = ListNode()

    def search(self, target: int) -> bool:
        cur = self.root
        while cur:
            if not cur.next:
                cur = cur.down
            elif target > cur.next.val:
                cur = cur.next
            elif target == cur.next.val:
                return True
            else:
                cur = cur.down
        return False

    def add(self, num: int) -> None:
        stack = []
        cur = self.root
        while cur:
            if not cur.next:
                stack.append(cur)
                cur = cur.down
            elif num > cur.next.val:
                cur = cur.next
            else:
                stack.append(cur)
                cur = cur.down
        down_node = None
        while stack:
            node = stack.pop()
            node.next = ListNode(val=num, next=node.next, down=down_node)
            down_node = node
            if random.randint(0, 1) == 0:
                break
            if not stack:
                self.root = ListNode(down=self.root)

    def erase(self, num: int) -> bool:
        stack = []
        cur = self.root
        while cur:
            if not cur.next:
                cur = cur.down
            elif num > cur.next.val:
                cur = cur.next
            elif num == cur.next.val:
                stack.append(cur)
                cur = cur.down
            else:
                cur = cur.down
        if not stack:
            return False
        while stack:
            node = stack.pop()
            node.next = node.next.next
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

# time O(logn) for all on average, worst is O(n)
# space O(n) on average, worst is O(nlogn)
# using linked list and skiplist and random
```