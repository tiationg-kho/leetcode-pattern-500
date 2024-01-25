from collections import defaultdict
import string
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        element_freq = defaultdict(int)
        mul_stack = []
        num = ''
        element = ''
        mul = 1
        for i in range(len(formula) - 1, - 1, - 1):
            c = formula[i]
            if c == ')':
                mul *= int(num) if num else 1
                mul_stack.append(int(num) if num else 1)
                num = ''
            elif c == '(':
                mul //= mul_stack.pop()
            elif c.isdigit():
                num = c + num
            else:
                element = c + element
                if c in string.ascii_uppercase:
                    element_freq[element] += mul * (int(num) if num else 1) 
                    element = ''
                    num = ''

        res = ''
        for e, f in sorted(element_freq.items()):
            res += e + (str(f) if f != 1 else '')
        return res
        
# time O(nlogn)
# space O(n), due to stack and hashmap
# using stack and queue and use stack to store the last states and hashmap and sort