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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        ArrayDeque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            ArrayList<Integer> cur = new ArrayList<>();
            int levelCount = queue.size();
            for (int i = 0; i < levelCount; i++) {
                TreeNode node = queue.poll();
                cur.add(node.val);
                for (TreeNode child: new TreeNode[]{node.left, node.right}) {
                    if (child != null) {
                        queue.offer(child);
                    }
                }
            }
            res.add(cur);
        }
        return res;
    }
}

// time O(n), due to traversal
// space O(n), queue can have a size of n/2 or the list's size to store nodes
// using tree and bfs