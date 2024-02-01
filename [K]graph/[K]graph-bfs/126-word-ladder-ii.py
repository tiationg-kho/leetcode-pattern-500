from collections import defaultdict, deque
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        wordset = set(wordList)
        queue = deque([beginWord])
        while queue:
            length = len(queue)
            next_queue = set()
            remove_wordset = set()
            found = False
            for _ in range(length):
                word = queue.popleft()
                if word == endWord:
                    found = True
                    break
                for replace_i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[: replace_i] + c + word[replace_i + 1:]
                        if new_word in wordset:
                            next_queue.add(new_word)
                            remove_wordset.add(new_word)
                            graph[new_word].append(word)
            if found:
                break
            wordset -= remove_wordset
            queue.extend(next_queue)

        res = []
        def dfs(path):
            if path[- 1] == beginWord:
                res.append(path[:: - 1])
                return
            for neighbor in graph[path[- 1]]:
                path.append(neighbor)
                dfs(path)
                path.pop()

        dfs([endWord])
        return res

# time O(n * L**2 + nL * 26**L), n * L**2 for bfs and building graph
# space O(nL), not couning output
# using graph and bfs with hashset as queue and hashset and dfs and backtracking
'''
1. bfs to build graph
2. dfs and backtracking to get all paths
'''