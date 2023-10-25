# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_dummy = odd_cur = ListNode()
        even_dummy = even_cur = ListNode()
        cur = head
        isOdd = True
        while cur:
            if isOdd:
                odd_cur.next = cur
                odd_cur = odd_cur.next
            else:
                even_cur.next = cur
                even_cur = even_cur.next
            cur = cur.next
            isOdd = not isOdd
        odd_cur.next = even_dummy.next
        even_cur.next = None
        return odd_dummy.next
        
# time O(n), due to traverse
# space (1)
# using linked list and sentinel nodes and multi pointers