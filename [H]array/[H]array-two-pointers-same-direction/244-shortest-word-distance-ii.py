from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.word_indices[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]

        res = float('inf')
        p1, p2 = 0, 0
        while p1 < len(indices1) and p2 < len(indices2):
            res = min(res, abs(indices1[p1] - indices2[p2]))
            if indices1[p1] < indices2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# time O(n) for init, O(f1 +f2) for shortest(), f1 and f2 is the freqence of word1 and word2
# space O(n)
# using array and two pointers same direction and traverse two sequences and hashmap