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
  public TreeNode invertTree(TreeNode root) {
      return helper(root);
  }

  public TreeNode helper(TreeNode node) {
      if (node == null) {
          return node;
      }
      TreeNode newLeft = node.right;
      TreeNode newRight = node.left;
      node.left = newLeft;
      node.right = newRight;
      helper(node.left);
      helper(node.right);
      return node;
  }
}

// time O(n)
// space O(n)
// using tree and dfs (preorder and recursive)