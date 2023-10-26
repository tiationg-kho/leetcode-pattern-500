from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        pattern_strings = defaultdict(list)

        for s in strings:
            new_s = ''
            shift = ord(s[0]) - ord('a')
            for c in s:
                new_c = chr((ord(c) - ord('a') - shift + 26) % 26 + ord('a'))
                new_s += new_c
            pattern_strings[new_s].append(s)

        return list(pattern_strings.values())

# time O(nL)
# space O(nL)
# using hashmap and store val