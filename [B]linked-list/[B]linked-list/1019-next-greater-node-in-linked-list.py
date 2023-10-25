# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        res = [0 for _ in range(count)]

        stack = []
        cur = head
        for i in range(count):
            while stack and stack[- 1][1] < cur.val:
                prev_idx, prev_val = stack.pop()
                res[prev_idx] = cur.val
            stack.append((i, cur.val))
            cur = cur.next
        return res
    
# time O(n)
# space O(n)
# using linked list and counting length and monotonic stack