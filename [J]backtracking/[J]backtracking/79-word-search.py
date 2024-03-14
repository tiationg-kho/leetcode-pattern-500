from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        schar_freq = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                schar_freq[board[r][c]] += 1
        tchar_freq = defaultdict(int)
        for c in word:
            tchar_freq[c] += 1
        for tc, freq in tchar_freq.items():
            if freq > schar_freq[tc]:
                return False
        
        def dfs(r, c, idx, visited):
            if idx == len(word):
                return True
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or board[next_r][next_c] != word[idx]:
                    continue
                visited.add((next_r, next_c))
                if dfs(next_r, next_c, idx + 1, visited):
                    return True
                visited.remove((next_r, next_c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1, {(r, c)}):
                        return True
        return False
    
# time O(RC * 3**L)
# space O(RC), due to hashset
# using dfs and backtracking and backtracking with constraints and pruning