from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        word_simword = defaultdict(set)
        for w1, w2 in similarPairs:
            word_simword[w1].add(w2)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2 or w2 in word_simword[w1] or w1 in word_simword[w2]:
                continue
            else:
                return False
        return True
    
# time O((p + n) * L), L is the avg length of words
# space O(p), p is the length of pairs (also the hashmap's size)
# using hashmap and store val and hashset