# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, cur, old_head = None, head, head
        count = 0
        while cur:
            count += 1
            prev = cur
            cur = cur.next
        old_tail = prev

        k %= count
        if k == 0:
            return head
            
        step = k + 1
        dummy = prev = cur = ListNode(next=head)
        while step:
            cur = cur.next
            step -= 1
        while cur:
            prev = prev.next
            cur = cur.next
        new_tail = prev
        new_head = prev.next
        old_tail.next = old_head
        new_tail.next = None
        return new_head
        
# time O(n)
# space O(1)
# using linked list and counting length and two pointers