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
    public boolean isBalanced(TreeNode root) {
        int[] res = dfs(root);
        if (res[1] == 1) {
            return true;
        }
        return false;
    }

    public int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[]{0, 1};
        }
        int[] left = dfs(node.left);
        int[] right = dfs(node.right);
        if (left[1] == 0 || right[1] == 0) {
            return new int[]{0, 0};
        }
        if (Math.abs(left[0] - right[0]) > 1) {
            return new int[]{0, 0};
        }
        return new int[]{Math.max(left[0], right[0]) + 1, 1};
    }
}

// time O(n), due to traverse
// space O(n), due to skewed tree's tree height (recursion stack)
// using tree and dfs (postorder and recursive)