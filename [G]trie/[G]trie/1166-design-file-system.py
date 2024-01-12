class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = - 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path, val):
        path = path.split('/')[1:]
        node = self.root
        for i, p in enumerate(path):
            if p not in node.children:
                if i == len(path) - 1:
                    node.children[p] = TrieNode()
                else:
                    return False
            node = node.children[p]
        if node.val == - 1:
            node.val = val
            return True
        else:
            return False

    def search(self, path):
        path = path.split('/')[1:]
        node = self.root
        for p in path:
            if p not in node.children:
                return - 1
            node = node.children[p]
        return node.val

class FileSystem:
    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value)

    def get(self, path: str) -> int:
        return self.trie.search(path)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# time O(1) for init, O(L) for createPath() and get()
# space O(nL)
# using trie and custom trie node