/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int res;

    public int diameterOfBinaryTree(TreeNode root) {
        res = 0;
        dfs(root);
        return res;
    }

    public int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftL = dfs(node.left);
        int rightL = dfs(node.right);
        int nodeAsPeakL = leftL + rightL;
        res = Math.max(res, nodeAsPeakL);
        return Math.max(leftL + 1, rightL + 1);
    }
}

// time O(n), due to traverse
// space O(n), due to tree height for skewed tree
// using tree and dfs (postorder, recursive)