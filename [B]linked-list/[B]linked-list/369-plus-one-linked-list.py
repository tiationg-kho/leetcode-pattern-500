# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(val=1, next=head)
        cur = head
        non_nine = None
        while cur:
            if cur.val != 9:
                non_nine = cur
            cur = cur.next
        
        if not non_nine:
            cur = head
            while cur:
                cur.val = 0
                cur = cur.next
            return dummy
        
        non_nine.val += 1
        while non_nine.next:
            non_nine.next.val = 0
            non_nine = non_nine.next
        return dummy.next

# time O(n)
# space O(1)
# using linked list and math and senitel node
'''
1. 999 -> 1000
2. 997 -> 998
3. 979 -> 980
'''