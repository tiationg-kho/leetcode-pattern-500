class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hash = 1009
        self.buckets = [None for _ in range(self.hash)]

    def add(self, key: int) -> None:
        idx = key % self.hash
        if self.buckets[idx] != None:
            node = self.buckets[idx]
            prev, cur, find = self.check(key, node)
            if not find:
                self.buckets[idx] = ListNode(key, node)
        else:
            self.buckets[idx] = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % self.hash
        if self.buckets[idx] != None:
            node = self.buckets[idx]
            prev, cur, find = self.check(key, node)
            if find:
                if prev:
                    prev.next = cur.next
                else:
                    self.buckets[idx] = cur.next

    def contains(self, key: int) -> bool:
        idx = key % self.hash
        if self.buckets[idx] != None:
            node = self.buckets[idx]
            prev, cur, find = self.check(key, node)
            return find
        else:
            return False
        
    def check(self, val, node):
        prev, cur, find = None, node, False
        while cur:
            if cur.val == val:
                find = True
                break
            prev = cur
            cur = cur.next
        return prev, cur, find

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# time O(n/k), k is the number of buckets, n/k is the length of linked list in bucket
# space O(n + k)
# using hahsmap and separate chaining and linked list and two pointers