class ListNode:
    def __init__(self, freq=- 1):
        self.freq = freq
        self.set = set()
        self.prev = None
        self.next = None

class Dll:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert_first(self, node):
        prev_node = self.head
        next_node = self.head.next
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node

    def insert_before(self, old_node, new_node):
        prev_node = old_node.prev
        node = new_node
        next_node = old_node
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node

    def insert_after(self, old_node, new_node):
        prev_node = old_node
        node = new_node
        next_node = old_node.next
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node
    
    def get_first_node(self):
        return self.head.next

    def get_last_node(self):
        return self.tail.prev

class AllOne:

    def __init__(self):
        self.dll = Dll()
        self.key_node = {}
        self.freq_node = {}

    def inc(self, key: str) -> None:
        if key not in self.key_node:
            if 1 not in self.freq_node:
                node = ListNode(1)
                node.set.add(key)
                self.dll.insert_first(node)
                self.key_node[key] = node
                self.freq_node[1] = node
            else:
                node = self.freq_node[1]
                node.set.add(key)
                self.key_node[key] = node
        else:
            old_node = self.key_node[key]
            old_freq = old_node.freq
            old_node.set.remove(key)
            new_freq = old_freq + 1

            if new_freq not in self.freq_node:
                node = ListNode(new_freq)
                node.set.add(key)
                self.dll.insert_after(old_node, node)
                self.key_node[key] = node
                self.freq_node[new_freq] = node
            else:
                node = self.freq_node[new_freq]
                node.set.add(key)
                self.key_node[key] = node

            if len(old_node.set) == 0:
                self.dll.remove(old_node)
                self.freq_node.pop(old_freq)
                

    def dec(self, key: str) -> None:
        old_node = self.key_node[key]
        old_freq = old_node.freq
        old_node.set.remove(key)
        new_freq = old_freq - 1

        if new_freq == 0:
            self.key_node.pop(key)
        elif new_freq not in self.freq_node:
            node = ListNode(new_freq)
            node.set.add(key)
            self.dll.insert_before(old_node, node)
            self.key_node[key] = node
            self.freq_node[new_freq] = node
        else:
            node = self.freq_node[new_freq]
            node.set.add(key)
            self.key_node[key] = node

        if len(old_node.set) == 0:
            self.dll.remove(old_node)
            self.freq_node.pop(old_freq)

    def getMaxKey(self) -> str:
        node = self.dll.get_last_node()
        if node.freq == - 1:
            return ""
        hashset = node.set
        res = hashset.pop()
        hashset.add(res)
        return res

    def getMinKey(self) -> str:
        node = self.dll.get_first_node()
        if node.freq == - 1:
            return ""
        hashset = node.set
        res = hashset.pop()
        hashset.add(res)
        return res

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# time O(1)
# space O(n)
# using linked list and dll and hashmap
'''
1. maintain key_node hashmap
2. maintain freq_node hashmap
3. maintain dll
'''