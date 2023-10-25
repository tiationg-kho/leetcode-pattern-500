# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = prev = ListNode(next=head)
        cur = head
        count = 0
        group = 1
        while cur:
            count += 1
            if count == 1:
                prev_nodes = prev
                old_head = cur
            if count == group and group % 2:
                count = 0
                group += 1
                prev = cur
                cur = cur.next
            elif count == group and group % 2 == 0:
                old_tail = cur
                next_nodes = cur.next
                prev, cur = self.reverse(prev_nodes, old_head, old_tail, next_nodes)
                count = 0
                group += 1
            elif not cur.next and count % 2 == 0:
                old_tail = cur
                next_nodes = cur.next
                prev, cur = self.reverse(prev_nodes, old_head, old_tail, next_nodes)
            else:
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
        prev_nodes.next = prev
        old_head.next = next_nodes
        return old_head, next_nodes
    
# time O(n)
# space O(1)
# using linked list and two pointers (prev and cur) and multi pointers