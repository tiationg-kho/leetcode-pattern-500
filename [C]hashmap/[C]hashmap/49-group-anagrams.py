from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern_words = defaultdict(list)
        for word in strs:
            char_freq = [0 for _ in range(26)]
            for c in word:
                char_freq[ord(c) - ord('a')] += 1
            pattern_words[tuple(char_freq)].append(word)
        return list(pattern_words.values())

# time O(nL)
# space O(nL)
# using hashmap