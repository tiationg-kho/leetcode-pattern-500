# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i))
        dummy = cur = ListNode()
        while heap:
            val, i = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                heappush(heap, (lists[i].val, i))

        return dummy.next

# time O(nlogk), n is the number of nodes, k is the number of lists
# space O(k)
# using heap and k way merge problem and linked list