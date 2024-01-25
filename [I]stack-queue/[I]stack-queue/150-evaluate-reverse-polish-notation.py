class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        cal_stack = []
        for t in tokens:
            if t in '+-*/':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                if t == '+':
                    num_stack.append(num1 + num2)
                elif t == '-':
                    num_stack.append(num1 - num2)
                elif t == '*':
                    num_stack.append(num1 * num2)
                else:
                    num_stack.append(int(num1 / num2))
            else:
                num_stack.append(int(t))
        return num_stack[- 1]
    
# time O(n), due to traverse
# space O(n), due to stack
# using stack and queue and use stack to store the last states