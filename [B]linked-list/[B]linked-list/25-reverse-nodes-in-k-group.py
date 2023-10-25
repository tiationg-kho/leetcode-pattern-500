# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        
        dummy = prev = ListNode(next=head)
        cur = head
        prev_nodes, old_head, old_tail, next_nodes = None, None, None, None
        count = 0
        while cur:
            count += 1
            if count == 1:
                prev_nodes = prev
                old_head = cur
            if count == k:
                old_tail = cur
                next_nodes = cur.next
                prev, cur = self.reverse(prev_nodes, old_head, old_tail, next_nodes)
                count = 0
                continue
            prev = cur
            cur = cur.next

        return dummy.next

    def reverse(self, prev_nodes, old_head, old_tail, next_nodes):
        prev, cur = prev_nodes, old_head
        while cur and cur != next_nodes:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        prev_nodes.next = old_tail
        old_head.next = next_nodes
        return old_head, next_nodes
    
# time O(n)
# space O(1)
# using linked list and two pointers (prev and cur)