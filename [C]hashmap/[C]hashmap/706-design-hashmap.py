class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hash = 1009
        self.buckets = [None for _ in range(self.hash)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.hash
        if self.buckets[idx] != None:
            node = self.buckets[idx]
            prev, cur, find = self.check(key, node)
            if find:
                cur.val = value
            else:
                self.buckets[idx] = ListNode(key, value, node)
        else:
            self.buckets[idx] = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.hash
        if self.buckets[idx] != None:
            node = self.buckets[idx]
            prev, cur, find = self.check(key, node)
            if find:
                return cur.val
        return - 1

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

    def check(self, key, node):
        prev, cur, find = None, node, False
        while cur:
            if cur.key == key:
                find = True
                break
            prev = cur
            cur = cur.next
        return prev, cur, find

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# time O(n/k), k is the number of buckets, n/k is the length of linked list in bucket
# space O(n + k)
# using hahsmap and separate chaining and linked list and two pointers