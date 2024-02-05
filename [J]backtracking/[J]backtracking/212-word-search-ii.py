class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(path, r, c, visited, node, parent_node):
            if node.is_word:
                res.append(''.join(path))
                node.is_word = False
            if len(node.children) == 0:
                parent_node.children.pop(board[r][c])
                return
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or board[next_r][next_c] not in node.children:
                    continue
                visited.add((next_r, next_c))
                path.append(board[next_r][next_c])
                dfs(path, next_r, next_c, visited, node.children[board[next_r][next_c]], node)
                visited.remove((next_r, next_c))
                path.pop()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs([board[r][c]], r, c, {(r, c)}, trie.root.children[board[r][c]], trie.root)
        return res
                
# time O(RC * 3**L), L is the longest word's length
# space O(nL), due to trie
# using dfs and backtracking and backtracking with constraints and trie and pruning