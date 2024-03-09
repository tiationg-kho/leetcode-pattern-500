/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p, q);
    }

    public TreeNode dfs(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null) {
            return node;
        }
        TreeNode leftCand = dfs(node.left, p, q);
        TreeNode rightCand = dfs(node.right, p, q);
        if (leftCand != null && rightCand != null) {
            return node;
        }
        if (node.val == p.val || node.val == q.val) {
            return node;
        }
        if (leftCand != null) {
            return leftCand;
        }
        if (rightCand != null) {
            return rightCand;
        }
        return null;
    }
}

// time O(n)
// space O(n)
// using tree and dfs (postorder and recursive)
/*
1. dfs postorder (bottom up approach), helps to get the potential LCA info
*/