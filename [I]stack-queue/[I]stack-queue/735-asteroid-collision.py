class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for weight in asteroids:
            if not stack:
                stack.append(weight)
            elif stack[- 1] < 0:
                stack.append(weight)
            elif stack[- 1] > 0 and weight > 0:
                stack.append(weight)
            else:
                while stack and stack[- 1] > 0 and weight < 0:
                    if stack[- 1] > abs(weight):
                        weight = 0
                        break
                    elif stack[- 1] == abs(weight):
                        weight = 0
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if weight:
                    stack.append(weight)
        return stack
                  
# time O(n), each asteroid push and pop at most once
# space O(n), due to stack
# using stack and queue and use stack to store the last states