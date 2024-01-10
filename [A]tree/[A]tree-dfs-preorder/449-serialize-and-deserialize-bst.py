# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def int_to_string(val):
            byte_array = [(val >> (i * 8)) & 0xFF for i in range(4)][:: - 1]
            char_array = [chr(byte) for byte in byte_array]
            string = ''.join(char_array)
            return string

        def build(node):
            if not node:
                return ''
            cur = int_to_string(node.val)
            left = build(node.left)
            right = build(node.right)
            return cur + left + right
        
        return build(root)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def string_to_int(string):
            res = []
            val = 0
            for i, c in enumerate(string):
                val += ord(c) << (8 * (4 - 1 - (i % 4)))
                if i % 4 == 3:
                    res.append(val)
                    val = 0
            return res
        
        vals = string_to_int(data)
        idx = 0
        def build(lower, upper):
            nonlocal idx
            if idx >= len(vals):
                return None
            if vals[idx] <= lower or vals[idx] >= upper:
                return None
            node = TreeNode(vals[idx])
            idx += 1
            node.left = build(lower, node.val)
            node.right = build(node.val, upper)
            return node
        
        return build(float('-inf'), float('inf'))
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive) and turn tree to string and bst and bit manipulate
'''
1. tree is BST, so we can use comparsion of vals to avoid record null val as encoded string
2. turn every val into string (length: 4) by bit manipulation to make encoded string compact
'''