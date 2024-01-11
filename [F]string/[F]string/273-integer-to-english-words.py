class Solution:
    def numberToWords(self, num: int) -> str:
        singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        bases = ["", "", "Hundred", "Thousand", "", "", "Million", "", "", "Billion"]

        if num == 0:
            return "Zero"

        def helper(num):
            res = ""
            if num >= 10 ** 2:
                d, m = divmod(num, 10 ** 2)
                res += singles[d] + " " + bases[2] + " "
                num = m
            if num >= 10 * 2:
                d, m = divmod(num, 10)
                res += tens[d] + " "
                num = m
            res += singles[num] + " "
            return res.strip()

        res = ""
        for i in range(3, - 1, - 1):
            if num >= 10 ** (3 * i):
                d, m = divmod(num, 10 ** (3 * i))
                res += helper(d) + " " + bases[3 * i] + " "
                num = m
        return res.strip()
        
# time O(1)
# space O(1)
# using string and string composition