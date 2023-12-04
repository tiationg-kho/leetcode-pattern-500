# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def rev_group(prev_nodes, old_start, old_end, next_nodes):

            prev = None
            cur = old_start
            while cur and cur != next_nodes:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            new_start = prev
            new_end = old_start
            prev_nodes.next = new_start
            new_end.next = next_nodes

            return new_end, next_nodes

        
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = head
        prev_nodes = None
        old_start = None
        old_end = None
        next_nodes = None
        count = 0
        while cur:
            count += 1
            if count == 1:
                prev_nodes = prev
                old_start = cur
            if count == k:
                old_end = cur
                next_nodes = cur.next
                prev, cur = rev_group(prev_nodes, old_start, old_end, next_nodes)
                count = 0
            else:
                prev, cur = cur, cur.next
        return dummy.next
    
# time O(n)
# space O(1)
# using linked list and two pointers (prev and cur)