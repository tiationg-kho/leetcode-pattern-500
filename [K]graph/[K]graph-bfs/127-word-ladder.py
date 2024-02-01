from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        queue = deque([(beginWord, 1)])
        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            for replace_i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[: replace_i] + c + word[replace_i + 1:]
                    if new_word in wordset:
                        queue.append((new_word, count + 1))
                        wordset.remove(new_word)
        return 0
    
# time O(n * L**2)
# space O(nL), due to hashset
# using graph and bfs with single source