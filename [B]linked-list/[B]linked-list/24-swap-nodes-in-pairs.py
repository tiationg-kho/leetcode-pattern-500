# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = prev = ListNode(next=head)
        first = head
        second = head.next
        while first and second:
            nxt = second.next
            prev.next = second
            second.next = first
            first.next = nxt
            prev = first
            first = prev.next
            second = first.next if first else None
        return dummy.next
        
# time O(n)
# space O(1)
# using linked list and two pointers (prev and cur) and dummy node