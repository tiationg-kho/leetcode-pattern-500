from collections import defaultdict
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban_set = set(banned)
        word_freq = defaultdict(int)
        word = ''
        res = ''
        res_freq = 0
        for c in paragraph + ' ':
            if c in string.ascii_letters:
                word += c.lower()
            elif word:
                if word in ban_set:
                    word = ''
                    continue
                word_freq[word] += 1
                if word_freq[word] > res_freq:
                    res = word
                    res_freq = word_freq[word]
                word = ''

        return res

# time O(n+m)
# space O(n+m)
# using hashmap and store sth’s freq