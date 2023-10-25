# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(val=float('-inf'), next=head)
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = None
                cur = cur.next
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
                
        return dummy.next
    
# time O(n)
# space O(1)
# using linked lsit and two pointers (prev and cur) and sentinel node