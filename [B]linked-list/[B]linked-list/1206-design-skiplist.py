import random

class ListNode:
    def __init__(self, val=None, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

class Skiplist:

    def __init__(self):
        self.root = ListNode()

    def search(self, target: int) -> bool:
        cur = self.root
        while cur:
            if not cur.next:
                cur = cur.down
            elif target > cur.next.val:
                cur = cur.next
            elif target == cur.next.val:
                return True
            else:
                cur = cur.down
        return False

    def add(self, num: int) -> None:
        stack = []
        cur = self.root
        while cur:
            if not cur.next:
                stack.append(cur)
                cur = cur.down
            elif num > cur.next.val:
                cur = cur.next
            else:
                stack.append(cur)
                cur = cur.down
        down_node = None
        while stack:
            node = stack.pop()
            node.next = ListNode(val=num, next=node.next, down=down_node)
            down_node = node
            if random.randint(0, 1) == 0:
                break
            if not stack:
                self.root = ListNode(down=self.root)

    def erase(self, num: int) -> bool:
        stack = []
        cur = self.root
        while cur:
            if not cur.next:
                cur = cur.down
            elif num > cur.next.val:
                cur = cur.next
            elif num == cur.next.val:
                stack.append(cur)
                cur = cur.down
            else:
                cur = cur.down
        if not stack:
            return False
        while stack:
            node = stack.pop()
            node.next = node.next.next
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

# time O(logn) for all on average, worst is O(n)
# space O(n) on average, worst is O(nlogn)
# using linked list and skiplist and random