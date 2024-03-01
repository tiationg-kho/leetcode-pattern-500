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

    record Pair(TreeNode node, int level) { };

    public int maxDepth(TreeNode root) {
        int res = 0;
        if (root == null) {
            return 0;
        }
        ArrayDeque<Pair> queue = new ArrayDeque<>();
        queue.offer(new Pair(root, 1));
        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            TreeNode node = pair.node;
            int level = pair.level;
            res = Math.max(res, level);
            for (TreeNode child: new TreeNode[]{node.left, node.right}) {
                if (child != null) {
                    queue.offer(new Pair(child, level + 1));
                }
            }
        }
        return res;
    }
}

// time O(n), due to bfs
// space O(n), due to queue's size, it can be n/2 in a balanced tree's deepest level
// using tree and bfs