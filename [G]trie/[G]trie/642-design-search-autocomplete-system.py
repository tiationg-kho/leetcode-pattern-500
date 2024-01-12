class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentence = ''
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cur = self.root
        self.sentence = ''

    def insert(self, s, count):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.sentence = s
        node.count += count

    def search(self, char):
        if char == '#':
            self.insert(self.sentence, 1)
            self.cur = self.root
            self.sentence = ''
            return []
        elif not self.cur or char not in self.cur.children:
            self.cur = None
            self.sentence += char
            return []
        else:
            self.cur = self.cur.children[char]
            self.sentence += char
            res = self.search_helper(self.cur)
            res.sort(key = lambda x: (- x[0], x[1]))
            return [sentence for _, sentence in res[:3]]

    def search_helper(self, node):
        res = []
        if node.sentence:
            res.append((node.count, node.sentence))
        for child in node.children.values():
            res.extend(self.search_helper(child))
        return res

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for s, t in zip(sentences, times):
            self.trie.insert(s, t)

    def input(self, c: str) -> List[str]:
        return self.trie.search(c)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# time O(nL) for init(), O(nL + nlogn) or O(L) for input()
# space O(nL+s), s is the number of calling input(), we can store more info inside trie node for improving time complexity
# using trie and perform dfs inside trie and sort