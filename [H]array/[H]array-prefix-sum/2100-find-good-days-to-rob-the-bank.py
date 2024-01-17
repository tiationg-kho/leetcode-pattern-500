class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        inc_prefix = [0 for _ in range(len(security))]
        dec_prefix = [0 for _ in range(len(security))]

        inc = 0
        dec = 0
        for i in range(1, len(security)):
            if security[i - 1] > security[i]:
                dec += 1
            elif security[i - 1] < security[i]:
                inc += 1
            dec_prefix[i] = dec
            inc_prefix[i] = inc

        res = []
        for i in range(time, len(security) - time):
            inc_before = inc_prefix[i] - inc_prefix[i - time]
            dec_after = dec_prefix[i + time] - dec_prefix[i]

            if inc_before == 0 and dec_after == 0:
                res.append(i)

        return res
    
# time O(n)
# space O(n)
# using array and prefix sum and standard prefix sum