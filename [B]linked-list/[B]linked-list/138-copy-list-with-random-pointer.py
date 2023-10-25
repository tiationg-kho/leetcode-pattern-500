"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        old_node = head
        while old_node:
            next_old_node = old_node.next
            old_node.next = Node(x=old_node.val, next=next_old_node)
            old_node = next_old_node
        
        old_node = head
        while old_node:
            new_node = old_node.next
            next_old_node = old_node.next.next
            new_node.random = old_node.random.next if old_node.random else None
            old_node = next_old_node

        old_node = head
        new_list = head.next
        while old_node:
            new_node = old_node.next
            next_old_node = old_node.next.next
            old_node.next = next_old_node
            new_node.next = next_old_node.next if next_old_node else None
            old_node = next_old_node
        return new_list
        
# time O(n), due to traverse thrice
# space O(1), not count output list
# using linked list and interweaving
'''
0. OLD1 -> OLD2
1. creating and weaving: OLD1 -> NEW1 -> OLD2 -> NEW2
2. handle new_nodes' random ptr
3. unweaving and handle new_nodes' next ptr: OLD1 -> OLD2, NEW1 -> NEW2
'''