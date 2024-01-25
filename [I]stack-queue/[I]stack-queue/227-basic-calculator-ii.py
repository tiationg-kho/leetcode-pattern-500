class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        num_stack = []
        cal_stack = []

        def calc():
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            cal = cal_stack.pop()
            if cal == '+':
                num_stack.append(num1 + num2)
            elif cal == '-':
                num_stack.append(num1 - num2)
            elif cal == '*':
                num_stack.append(num1 * num2)
            else:
                num_stack.append(int(num1 / num2))
        
        cal_weight = {'+': 0, '-': 0, '*': 1, '/': 1}
        num = ''
        for i in range(len(s)):
            if s[i] in '+-*/':
                while cal_stack and cal_weight[cal_stack[- 1]] >= cal_weight[s[i]]:
                    calc()
                cal_stack.append(s[i])
            else:
                num += s[i]
                if i == len(s) - 1 or (i + 1 < len(s) and not s[i + 1].isdigit()):
                    num_stack.append(int(num))
                    num = ''
        
        while cal_stack:
            calc()

        return num_stack[- 1]
    
# time O(n)
# space O(n)
# using stack and queue and use stack to store the last states