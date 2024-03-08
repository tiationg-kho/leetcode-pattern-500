class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(res, candidates, target, new ArrayList<>(), 0, 0);
        return res;
    }

    public void dfs(List<List<Integer>> res, int[] candidates, int target, List<Integer> path, int total, int idx) {
        if (total == target) {
            res.add(new ArrayList<>(path));
            return;
        }
        if (total > target) {
            return;
        }
        for (int i = idx; i < candidates.length; i++) {
            path.add(candidates[i]);
            total += candidates[i];
            dfs(res, candidates, target, path, total, i);
            path.remove(path.size() - 1);
            total -= candidates[i];
        }
    }
}

// time O(n ** (T/S)), T is target number, and S is the min number in candidates
// space O(T/S), due to recursion stack
// using dfs and backtracking and subset
/*
1. type: subset
2. duplicate elements: no
3. selectable repeatedly: yes
*/