from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        
        used = set()
        stack = []
        for c in s:
            if c in used:
                char_freq[c] -= 1
                continue
            while stack and stack[- 1] > c and char_freq[stack[- 1]] >= 1:
                used.remove(stack[- 1])
                stack.pop()
            used.add(c)
            stack.append(c)
            char_freq[c] -= 1

        return ''.join(stack)
    
# time O(n)
# space O(n), or O(1) consider the number of letters
# using stack and queue and montonic and monotonic stack (consider one side’s relationship) and hashmap and hashset