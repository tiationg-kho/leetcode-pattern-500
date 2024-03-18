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
    int[] inorder;
    int[] postorder;
    int length;
    HashMap<Integer, Integer> invalToInidx;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.inorder = inorder;
        this.postorder = postorder;
        length = inorder.length;
        invalToInidx = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            invalToInidx.put(inorder[i], i);
        }
        return dfs(0, length - 1, 0, length - 1, length);
    }

    public TreeNode dfs(int inLeft, int inRight, int postLeft, int postRight, int length) {
        if (length < 1) {
            return null;
        }
        TreeNode node = new TreeNode(postorder[postRight]);
        int inidx = invalToInidx.get(postorder[postRight]);
        int leftLength = inidx - inLeft;
        int rightLength = inRight - inidx;
        node.left = dfs(inLeft, inidx - 1, postLeft, postLeft + leftLength - 1, leftLength);
        node.right = dfs(inidx + 1, inRight, postLeft + leftLength, postRight - 1, rightLength);
        return node;
    }
}

// time O(n)
// space O(n)
// using tree and divide and conquer and re-build tree (top-down)
/*
postorder: last value is root
inorder: every value before root is left subtree, after root is right subtree
*/