class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = - 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, idx):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.idx = idx

    def search(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                return - 1
            node = node.children[c]
        return node.idx

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, w in enumerate(words):
            for start in range(len(w)):
                self.trie.insert(w[start:] + '#' + w, i)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(suff + '#' + pref)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# time O(n(L**2)) for init, O(L) for f()
# space O(n(L**2))
# using trie and custom trie node
'''
1. search suffix first than prefix
2. because we don't know the chars between them
3. so we cannot search prefix first
'''