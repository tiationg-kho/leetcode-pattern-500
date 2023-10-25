# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, p1, p2 = ListNode(), list1, list2
        cur = dummy
        while p1 or p2:
            if p1 and p2 and p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
                cur = cur.next
            elif p1 and p2:
                cur.next = p2
                p2 = p2.next
                cur = cur.next
            elif p1:
                cur.next = p1
                break
            else:
                cur.next = p2
                break
        return dummy.next

                
# time O(m+n), m and n are the linked lists' size
# space O(1)
# using linked list and sentinel node