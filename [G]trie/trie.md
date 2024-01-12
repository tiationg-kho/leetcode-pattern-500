# trie

## intro

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# time O(L) for insert(), search(), startsWith(), L is the word's length
# space O(nL), n is the number of words, L is the max len
```

- concepts
    - trie is a prefix tree
        - can insert word, search word, and search prefix efficiently in `O(L)`
        - a tree of character nodes
        - every node has a hashmap for children nodes
    - prune
        - think about when we can stop finding deeper nodes
        - think about remove certain node which no longer need to be considered
    - trie's variation can happen in
        - trie node
        - inserting way
        - searching way

## pattern

- **standard trie**
    - insert word, search word, and search prefix
- **custom trie node**
    - the information to store in TrieNode can be different, depends on different problems
    - like store a list, boolean, string inside each trie node
        - notice the space complexity could increase
            - when disucss about complexity need to mention that only count for number of nodes or consider the content inside
    - store more info can improve time complexity sometimes
- **perform dfs inside trie**
    - can use dfs as assistance for searching (eg. args: node, idx)
    - could increase the time complexity for searching