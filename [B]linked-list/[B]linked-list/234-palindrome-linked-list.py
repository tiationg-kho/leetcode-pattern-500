# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head
        
        step = 0
        slow, fast = head, head
        while fast and fast.next:
            step += 1 
            slow = slow.next
            fast = fast.next.next
        second_part_old_head = slow

        prev, cur = None, second_part_old_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second_part_new_head = prev

        p1, p2 = head, second_part_new_head
        while step:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
            step -= 1
        return True
        
# time O(n)
# space O(1)
# using linked lsit and two pointers (utilize symmetry property) (finding middle, reversing, comparing)