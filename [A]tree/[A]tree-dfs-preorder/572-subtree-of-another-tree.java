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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        StringBuffer rootSb = new StringBuffer();
        build(root, rootSb);
        String s = rootSb.toString();

        StringBuffer subRootSb = new StringBuffer();
        build(subRoot, subRootSb);
        String t = subRootSb.toString();

        int base = 131;
        int mod = 1000000007;
        long target = 0;
        for (int i = 0; i < t.length(); i++) {
            target = (target * base + t.charAt(i)) % mod;
        }
        long val = 0;
        long removeVal = 1;
        for (int i = 0; i < t.length() - 1; i++) {
            removeVal = (removeVal * base) % mod;
        }
        for (int i = 0; i < s.length(); i++) {
            if (i >= t.length()) {
                val = (val - ((removeVal * s.charAt(i - t.length())) % mod) + mod) % mod;
            }
            val = (val * base + s.charAt(i)) % mod;
            if (i >= t.length() - 1) {
                if (val == target) {
                    return true;
                }
            }
        }
        return false;
    }

    public void build(TreeNode node, StringBuffer s) {
        if (node == null) {
            s.append("#n");
            return;
        }
        s.append("#");
        s.append(node.val + "");
        build(node.left, s);
        build(node.right, s);
        return;
    }
}

// time O(n+m)
// space O(n+m)
// using tree and dfs (preorder and recursive) and turn tree to string and rabin karp (rolling hash)