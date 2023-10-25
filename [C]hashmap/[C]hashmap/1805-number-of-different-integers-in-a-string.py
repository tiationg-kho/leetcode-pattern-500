class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        hashset = set()
        string = ''
        for c in word + ' ':
            if c.isdigit():
                string += c
            else:
                if string:
                    hashset.add(int(string))
                    string = ''
        
        return len(hashset)
    
# time O(n)
# space O(n)
# using hashmap and store val and string and hashset