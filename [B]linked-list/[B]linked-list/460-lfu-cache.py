class ListNode:
    def __init__(self, key=None, val=None, freq=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class Dll:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        prev_node = self.tail.prev
        next_node = self.tail
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node
        self.size += 1
        return node

    def popleft(self):
        prev_node = self.head
        node = self.head.next
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        return node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        return node

    def is_empty(self):
        return self.size == 0

class LFUCache:

    def __init__(self, capacity: int):
        self.key_node = {}
        self.freq_dll = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return - 1
        node = self.key_node[key]
        self.add_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.key_node:
            if len(self.key_node) == self.capacity:
                dll_for_pop = self.freq_dll[self.min_freq]
                remove_node = dll_for_pop.popleft()
                self.key_node.pop(remove_node.key)
                if dll_for_pop.is_empty():
                    self.freq_dll.pop(self.min_freq)
            self.min_freq = 1
            node = ListNode(key, value, 1)
            self.key_node[key] = node
            if 1 not in self.freq_dll:
                self.freq_dll[1] = Dll()
            dll = self.freq_dll[1]
            dll.append(node)
        else:
            node = self.key_node[key]
            node.val = value
            self.add_freq(node)

    def add_freq(self, node):
        old_freq = node.freq
        new_freq = old_freq + 1
        node.freq = new_freq
        old_dll = self.freq_dll[old_freq]
        old_dll.remove(node)
        if old_dll.is_empty():
            self.freq_dll.pop(old_freq)
            if old_freq == self.min_freq:
                self.min_freq = new_freq
        if new_freq not in self.freq_dll:
            self.freq_dll[new_freq] = Dll()
        new_dll = self.freq_dll[new_freq]
        new_dll.append(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# time O(1)
# space O(capacity)
# using linked list and dll and hashmap
'''
1. maintain key_node hashmap
2. maintain freq_dll hashmap
3. maintain min_freq variable (modify when add new node or add freq for node)
4. maintain capacity
5. if get() or put(), dll of cur freq remove used node, and append node to tail in another dll which belongs freq + 1
6. if exceed capacity, dll of min_freq popleft the least recent used node and pop it from hashmap
'''