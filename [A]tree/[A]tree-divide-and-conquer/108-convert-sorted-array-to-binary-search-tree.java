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
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(0, nums.length - 1, nums);
    }

    public TreeNode build(int left, int right, int[] nums) {
        if (left > right) {
            return null;
        }
        int m = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[m]);
        node.left = build(left, m - 1, nums);
        node.right = build(m + 1, right, nums);
        return node;
    }
}

// time O(n), due to traverse each node once
// space O(logn), due to memo stack's size, and output is O(n)
// using tree and divide and conquer and re-build BST (top-down approach)