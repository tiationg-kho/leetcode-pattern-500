class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                second_num = stack.pop()
                first_num = stack.pop()
                if t == '+':
                    stack.append(first_num + second_num)
                elif t == '-':
                    stack.append(first_num - second_num)
                elif t == '*':
                    stack.append(first_num * second_num)
                else:
                    stack.append(int(first_num / second_num))
            else:
                stack.append(int(t))

        return stack[- 1]
    
# time O(n), due to traverse
# space O(n), due to stack
# using stack and queue and use stack to store the last states