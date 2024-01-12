class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1
    
    def search(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.search(pref)

# time O(nL)
# space O(nL)
# using trie and custom trie node
'''
1. using trie allows we change requested prefix frequently
2. if prefix is fixed, and words are sorted. try binary search (O(klogn)))
'''