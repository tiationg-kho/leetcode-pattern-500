class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, s):
        return self.search_helper(s, self.root, 0)

    def search_helper(self, s, node, idx):
        for i in range(idx, len(s)):
            if s[i] == '.':
                for child in node.children.values():
                    if self.search_helper(s, child, i + 1):
                        return True
                return False
            if s[i] not in node.children:
                return False
            node = node.children[s[i]]
        return node.is_word

class WordDictionary:
    def __init__(self):
        self.trie = Trie()
        self.len_set = set()

    def addWord(self, word: str) -> None:
        self.len_set.add(len(word))
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        if len(word) not in self.len_set:
            return False
        return self.trie.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# time O(nL or 26**L) for search(), O(L) for addWord()
# space O(nL), n is the number of words, L is the max len
# using trie and perform dfs inside trie and prune