from collections import defaultdict
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        odd_char = None
        chars = []
        for c, f in char_freq.items():
            if f % 2:
                if odd_char != None:
                    return []
                odd_char = c
                chars.extend([c for _ in range((f - 1) // 2)])
            else:
                chars.extend([c for _ in range(f // 2)])
                
        res = []
        def dfs(path, visited):
            if len(path) == len(chars):
                if odd_char != None:
                    res.append(''.join(path) + odd_char + ''.join(path[::- 1]))      
                else:
                    res.append(''.join(path) + ''.join(path[::- 1]))
                return
            for i, c in enumerate(chars):
                if i - 1 >= 0 and chars[i - 1] == chars[i] and i - 1 not in visited:
                    continue
                if i not in visited:
                    path.append(chars[i])
                    visited.add(i)
                    dfs(path, visited)
                    path.pop()
                    visited.remove(i)
        
        dfs([], set())
        return res

# time O((n/2)! * n)
# space O(n/2), not count output
# using dfs and backtracking and hashmap and permutation
'''
1. type: permutation
2. duplicate elements: yes
3. selectable repeatedly: no
'''