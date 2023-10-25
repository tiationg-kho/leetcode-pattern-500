# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = cur = ListNode(next=head)
        step = n + 1
        while step:
            cur = cur.next
            step -= 1

        while cur:
            prev = prev.next
            cur = cur.next

        prev.next = prev.next.next
        return dummy.next
        
# time O(n)
# space O(1)
# using linked list and sentinel node and two pointers
'''
1. maintain two same direction pointers with n gap
2. once one ptr reach null, then another is nth from end
'''