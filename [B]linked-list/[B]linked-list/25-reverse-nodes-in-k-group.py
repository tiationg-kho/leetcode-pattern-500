# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev(prev_nodes, old_head, old_tail, next_nodes):
            prev = None
            cur = old_head
            while cur and cur != next_nodes:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            new_head = prev
            prev_nodes.next = new_head
            new_tail = old_head
            new_tail.next = next_nodes
            return new_tail

        dummy = ListNode(next=head)
        total = 0
        prev_nodes = dummy
        old_head = head
        cur = head
        while cur:
            total += 1
            if total == 1:
                old_head = cur
            if total == k:
                new_tail = rev(prev_nodes, old_head, cur, cur.next)
                prev_nodes = new_tail
                cur = new_tail
                total = 0
            cur = cur.next
        return dummy.next
    
# time O(n)
# space O(1)
# using linked list and two pointers (prev and cur)