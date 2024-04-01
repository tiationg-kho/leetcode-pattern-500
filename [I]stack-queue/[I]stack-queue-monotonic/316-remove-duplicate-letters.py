from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        stack = []
        visited = set()
        for c in s:
            while stack and char_freq[stack[- 1]] and stack[- 1] > c and c not in visited:
                remove_c = stack.pop()
                visited.remove(remove_c)
            if c not in visited:
                stack.append(c)
                visited.add(c)
            char_freq[c] -= 1
        return ''.join(stack)
    
# time O(n)
# space O(n), or O(1) consider the number of letters
# using stack and queue and montonic and monotonic stack (consider one side’s relationship) and hashmap and hashset