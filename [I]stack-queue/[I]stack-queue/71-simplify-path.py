class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split('/')[1:]

        for c in path:
            if not c or c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)
    
# time O(n), due to traverse and split
# space O(n), due to stack and split
# using stack and queue and use stack to store the last states