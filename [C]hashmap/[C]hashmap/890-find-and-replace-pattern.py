class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def check(p, q):
            pc_qc = {}
            qc_pc = {}
            for pc, qc in zip(p, q):
                if pc not in pc_qc:
                    pc_qc[pc] = qc
                if qc not in qc_pc:
                    qc_pc[qc] = pc
                if pc_qc[pc] != qc or qc_pc[qc] != pc:
                    return False
            return True

        return [w for w in words if check(w, pattern)]
    
# time O(nL), n is the number of words
# space O(1), not counting output
# using hashmap