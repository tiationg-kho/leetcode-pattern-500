class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggests = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.suggests.append(s)
            node.suggests = sorted(node.suggests)[:3]
    
    def search(self, s):
        res = []
        node = self.root
        for i, c in enumerate(s):
            if c not in node.children:
                res.extend([[] for _ in range(len(s) - i)])
                break
            node = node.children[c]
            res.append(node.suggests)
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.insert(p)
        return trie.search(searchWord)

# time O(nL)
# space O(nL), nL nodes in trie, not counting suggests list storage in node
# using trie and custom trie node and sort