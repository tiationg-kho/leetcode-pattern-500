class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_idx = {}
        for i, word in enumerate(words):
            word_idx[word] = i

        res = []
        for i, word in enumerate(words):
            rev_word = word[:: - 1]

            if word and word == rev_word and "" in word_idx:
                res.append([i, word_idx[""]])
                res.append([word_idx[""], i])

            if word and rev_word in word_idx and i != word_idx[rev_word]:
                res.append([i, word_idx[rev_word]])

            for cut in range(1, len(word)):
                prefix = word[0: cut]
                suffix = word[cut:]
                rev_prefix = prefix[:: - 1]
                rev_suffix = suffix[:: - 1]
                if suffix == rev_suffix and rev_prefix in word_idx:
                    res.append([i, word_idx[rev_prefix]])
                if prefix == rev_prefix and rev_suffix in word_idx:
                    res.append([word_idx[rev_suffix], i])
        
        return res
                    
# time O(n * (L**2))
# space O(nL), due to hashmap
# using hashmap and store val and palindrome
'''
we got 5 situations:
(notice word, prefix, suffix cannot be empty)
1. pal_word + ""
2. "" + pal_word
3. word + word[:: - 1]
4. prefix + pal_suffix + prefix[:: - 1]
5. suffix[:: - 1] + pal_prefix + suffix

how to check palindrome:
approach 1: use two pointers
approach 2: use word == word[:: - 1]
'''