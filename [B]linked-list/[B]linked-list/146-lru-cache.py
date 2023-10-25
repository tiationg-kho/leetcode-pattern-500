class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class Dll:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        prev_node = self.tail.prev
        next_node = self.tail
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node
        return node

    def popleft(self):
        prev_node = self.head
        node = self.head.next
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return node

    def update(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.append(node)
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.dll = Dll()
        self.key_node = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return - 1
        node = self.key_node[key]
        self.dll.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.key_node:
            if len(self.key_node) == self.capacity:
                remove_node = self.dll.popleft()
                self.key_node.pop(remove_node.key)
            node = self.dll.append(ListNode(key=key, val=value))
            self.key_node[key] = node
        else:
            node = self.key_node[key]
            node.val = value
            self.dll.update(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# time O(1)
# space O(capacity)
# using linked list and dll and hashmap
'''
1. maintain key_node hashmap
2. maintain dll
3. maintain capacity
4. if get() or put(), dll update the recent used node to the dll's tail or just append node to tail
5. if exceed capacity, dll popleft the least recent used node and pop it from hashmap
'''