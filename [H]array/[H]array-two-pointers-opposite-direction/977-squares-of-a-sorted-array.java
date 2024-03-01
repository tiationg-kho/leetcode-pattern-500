class Solution {
    public int[] sortedSquares(int[] nums) {
        List<Integer> list = new ArrayList<>();
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            if (Math.abs(nums[left]) > Math.abs(nums[right])) {
                list.add(nums[left] * nums[left]);
                left += 1;
            } else {
                list.add(nums[right] * nums[right]);
                right -= 1;
            }
        }
        Collections.reverse(list);
        return list.stream().mapToInt(i -> i).toArray();
    }
}

// time O(n)
// space O(n)
// using array and two pointers opposite direction and shrink type