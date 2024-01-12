class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.length = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for i, c in enumerate(s):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1
            node.length = i + 1

    def search(self, s):
        res = 0
        node = self.root
        for c in s:
            node = node.children[c]
            res += node.count
            if node.count == 1:
                res += len(s) - node.length
                break
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        res = []
        for w in words:
            res.append(trie.search(w))
        return res
    
# time O(nL)
# space O(nL)
# using trie and custom trie node and prune