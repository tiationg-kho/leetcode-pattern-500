# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(next=head)
        count = 0
        prev, cur = dummy, head
        prev_nodes, old_head, old_tail, next_nodes = None, None, None, None
        while cur:
            count += 1
            if left <= count <= right:
                if count == left:
                    prev_nodes = prev
                    old_head = cur
                if count == right:
                    old_tail = cur
                    next_nodes = cur.next
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            else:
                prev = cur
                cur = cur.next
                
        prev_nodes.next = old_tail
        old_head.next = next_nodes
        return dummy.next
    
# time O(n)
# space O(1)
# using linked list and two pointers (prev and cur) and multi pointers