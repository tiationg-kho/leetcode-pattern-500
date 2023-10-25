# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first_part_tail = slow
        second_part_old_head = slow.next
        first_part_tail.next = None

        prev, cur = None, second_part_old_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second_part_new_head = prev

        dummy = cur = ListNode()
        p1, p2 = head, second_part_new_head
        while p1 and p2:
            cur.next = p1
            p1 = p1.next
            cur = cur.next
            cur.next = p2
            p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        return
        
# time O(n)
# space O(1)
# using linked lsit and two pointers (utilize symmetry property) (finding middle, reversing, combining)