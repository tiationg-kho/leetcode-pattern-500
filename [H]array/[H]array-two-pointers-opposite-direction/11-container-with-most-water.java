class Solution {
    public int maxArea(int[] height) {
        int res = 0;
        int left = 0;
        int right = height.length - 1;
        while (left <= right) {
            int cur = Math.min(height[left], height[right]) * (right - left);
            res = Math.max(res, cur);
            if (height[left] > height[right]) {
                right -= 1;
            } else {
                left += 1;
            }
        }
        return res;
    }
}

// time O(n)
// space O(1)
// using array and two pointers opposite direction and shrink type and greedy