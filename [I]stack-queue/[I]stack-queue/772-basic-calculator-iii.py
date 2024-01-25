class Solution:
    def calculate(self, s: str) -> int:
        s = '(' + s + ')'

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
            if s[i] == '(':
                cal_stack.append(s[i])
            elif s[i] == ')':
                while cal_stack and cal_stack[- 1] != '(':
                    calc()
                cal_stack.pop()
            elif s[i] in '+-*/':
                while cal_stack and cal_stack[- 1] != '(' and cal_weight[cal_stack[- 1]] >= cal_weight[s[i]]:
                    calc()
                cal_stack.append(s[i])
            else:
                num += s[i]
                if not s[i + 1].isdigit():
                    num_stack.append(int(num))
                    num = ''
        return num_stack[- 1]
    
# time O(n)
# space O(n)
# using stack and queue and use stack to store the last states