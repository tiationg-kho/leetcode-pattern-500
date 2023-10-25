# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        val_freq = defaultdict(int)
        dummy = prev = ListNode(next=head)
        cur = head
        while cur:
            val_freq[cur.val] += 1
            cur = cur.next

        cur = head
        while cur:
            if val_freq[cur.val] >= 2:
                prev.next = None
                cur = cur.next
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        return dummy.next
    
# time O(n)
# space O(n)
# using linked list and two pointers (prev and cur) and hashmap