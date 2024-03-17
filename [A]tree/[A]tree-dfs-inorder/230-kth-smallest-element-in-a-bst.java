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
    public int kthSmallest(TreeNode root, int k) {
        int[] idxRes = new int[2];
        dfs(root, k, idxRes);
        return idxRes[1];
    }

    public void dfs(TreeNode node, int k, int[] idxRes) {
        if (node == null) {
            return;
        }
        dfs(node.left, k, idxRes);
        idxRes[0] += 1;
        if (idxRes[0] == k) {
            idxRes[1] = node.val;
            return;
        }
        dfs(node.right, k, idxRes);
        return;
    }
}

// time O(n), for skewed tree's height
// space O(n), due to memo stack's size for skewed tree's height 
// using tree and dfs (inorder and recursive)