class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res = []
        cur_words = []
        cur_len = 0
        for i, word in enumerate(words):
            if not cur_words or (cur_len + len(cur_words) + len(word) <= maxWidth):
                cur_words.append(word)
                cur_len += len(word)
            else:
                blank = maxWidth - cur_len
                if len(cur_words) > 1:
                    d, m = divmod(blank, len(cur_words) - 1)
                    tail = 0
                else:
                    d, m = 0, 0
                    tail = blank
                text = ''
                for j, w in enumerate(cur_words):
                    text += w
                    if j < len(cur_words) - 1:
                        text += ' ' * d
                        if m:
                            text += ' '
                            m -= 1
                    else:
                        text += ' ' * tail
                res.append(text)
                cur_words = [word]
                cur_len = len(word)
            if i == len(words) - 1:
                blank = maxWidth - cur_len
                text = ''
                for j, w in enumerate(cur_words):
                    text += w
                    if j < len(cur_words) - 1:
                        text += ' '
                        blank -= 1
                    else:
                        text += ' ' * blank
                res.append(text)
            
        return res

# time O(nL)
# space O(nL)
# using string and string composition
'''
1. fully justified: 
   contain >= 2 words: [word + blank + word]
   contain only 1 word: [word + blank] (blank can be empty here)
2. left justified: 
   contain >= 2 words: [word + 1 + word + blank] (blank can be empty here)
   contain only 1 word: [word + blank] (blank can be empty here)
'''