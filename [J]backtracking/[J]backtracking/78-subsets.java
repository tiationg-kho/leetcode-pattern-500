class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(res, nums, new ArrayList<>(), 0);
        return res;
    }

    public void dfs(List<List<Integer>> res, int[] nums, List<Integer> path, int idx) {
        if (idx == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }

        dfs(res, nums, path, idx + 1);

        path.add(nums[idx]);
        dfs(res, nums, path, idx + 1);
        path.remove(path.size() - 1);
        return;
    }
}

// time O(n*(2**n)), due to each element can take or not take (2**n), and n for copy list
// space O(n), due to recursion stack, not counting output here
// using dfs and backtracking and subset
/*
1. type: subset
2. duplicate elements: no
3. selectable repeatedly: no
*/
/*
this approach focus on considering each element:
for cur element, 
we don't take, then goto next element
or we take, then goto next element
till no more element to be considered, we record path
*/