class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, new ArrayList<>(), new HashSet<>(), res);
        return res;
    }

    public void dfs(int[] nums, ArrayList<Integer> path, HashSet<Integer> visited, List<List<Integer>> res) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!visited.contains(i)) {
                path.add(nums[i]);
                visited.add(i);
                dfs(nums, path, visited, res);
                path.remove(path.size() - 1);
                visited.remove(i);
            }
        }
    }
}

// time O(n*n!), dfs will calls n! times and each non-leaf node traverse list costs O(n) and leaf node copy a list to answer costs O(n)
// space O(n*n!), because answer contains n! permutations and each permutaiton can cost O(n). Besides, memory stack size is O(n)
// using dfs and backtracking and permutation
/*
1. type: permutation
2. duplicate elements: no
3. selectable repeatedly: no
*/