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
            if node.is_word:
                if self.search_helper(s, self.root, i):
                    return True
            if s[i] not in node.children:
                return False
            node = node.children[s[i]]
        return node.is_word

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        words.sort(key=len)
        for w in words:
            if trie.search(w):
                res.append(w)
            else:
                trie.insert(w)
            
        return res
        
# time O(nlogn + nL + n * L**2), search is O(L**2) here not O(2**L), due to cost is L + L-1 + L-2 + ... + 1
# space O(nL), n is the number of words, L is the max len
# using trie and perform dfs inside trie and sort
'''
1. long word can only be consisted from short words, so we sort at first
2. if certain word can be consisted from short words then no need to add in trie
'''