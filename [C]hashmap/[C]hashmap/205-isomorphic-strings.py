class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sc_tc = {}
        tc_sc = {}
        for sc, tc in zip(s, t):
            if sc not in sc_tc:
                sc_tc[sc] = tc
            if tc not in tc_sc:
                tc_sc[tc] = sc
            if sc_tc[sc] != tc or tc_sc[tc] != sc:
                return False
        return True
            
# time O(n), due to traverse
# space O(n), can be O(1) since char's number is limited
# using hashmap and build bijection mapping relation