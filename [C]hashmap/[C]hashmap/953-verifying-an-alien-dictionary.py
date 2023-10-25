class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_val = {}
        for i, c in enumerate(order):
            char_val[c] = i

        for i in range(len(words)):
            if i + 1 < len(words):
                cur_word = words[i]
                next_word = words[i + 1]
                j = 0
                while j < len(cur_word) and j < len(next_word):
                    if char_val[cur_word[j]] < char_val[next_word[j]]:
                        break
                    elif char_val[cur_word[j]] == char_val[next_word[j]]:
                        j += 1
                        if j < len(cur_word) and j >= len(next_word):
                            return False
                    else:
                        return False
        return True
        
# time O(nL), n is the number of words and L is the average length of words
# space O(1), hashmap's size is 26
# using hashmap and store val