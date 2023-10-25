# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# time O(n), due to traverse
# space O(1)
# using linked list and two pointers (slow and fast)
'''
1. If there are two middle nodes, return the second middle node: use 'while fast and fast.next'
2. If there are two middle nodes, return the first middle node: use 'while fast.next and fast.next.next'
'''