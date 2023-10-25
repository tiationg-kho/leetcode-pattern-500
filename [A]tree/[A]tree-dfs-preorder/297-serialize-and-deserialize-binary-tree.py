# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node:
                return '#null'
            cur = '#' + str(node.val)
            left = helper(node.left)
            right = helper(node.right)
            return cur + left + right
        
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split('#')[1:]
        idx = 0
        def helper():
            nonlocal idx
            val = vals[idx]
            idx += 1
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive) and turn tree to string