class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s

        rows = [[] for _ in range(numRows)]
        flag = 1
        idx = 0
        for c in s:
            rows[idx].append(c)
            if not (0 <= idx + flag < len(rows)):
                flag *= - 1
            idx += flag

        res = ''
        for row in rows:
            res += ''.join(row)
        return res

# time O(n)
# space O(n)
# using string and string composition