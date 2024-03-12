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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> inValToInIdx = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inValToInIdx.put(inorder[i], i);
        }
        return build(preorder, inValToInIdx, 0, preorder.length - 1, 0, inorder.length - 1, preorder.length);
    }

    public TreeNode build(int[] preorder, Map<Integer, Integer> inValToInIdx, int preLeft, int preRight, int inLeft, int inRight, int length) {
        if (length < 1) {
            return null;
        }
        TreeNode node = new TreeNode(preorder[preLeft]);
        Integer inIdx = inValToInIdx.get(preorder[preLeft]);
        int leftLength = inIdx - inLeft;
        int rightLength = length - leftLength - 1;
        node.left = build(preorder, inValToInIdx, preLeft + 1, preLeft + leftLength, inLeft, inIdx - 1, leftLength);
        node.right = build(preorder, inValToInIdx, preLeft + leftLength + 1, preRight, inIdx + 1, inRight, rightLength);
        return node;
    }
}

// time O(n), due to O(1) find in hashmap but recursion n times
// space O(n), due to hashmap or building tree or recursion
// using tree and divide and conquer and re-build tree (top-down)
/*
preorder: first value is root
inorder: every value before root is left subtree, after root is right subtree
*/