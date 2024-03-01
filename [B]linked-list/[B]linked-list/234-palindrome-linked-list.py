# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first_half_tail = slow
        second_half_head = first_half_tail.next

        prev = None
        cur = second_half_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        new_second_half_head = prev

        p1 = head
        p2 = new_second_half_head
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        
# time O(n)
# space O(1)
# using linked lsit and two pointers (utilize symmetry property) (finding middle, reversing, comparing)