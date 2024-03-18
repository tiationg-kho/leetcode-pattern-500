class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int left = 0;
        int right = rows * cols - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            int r = m / cols;
            int c = m % cols;
            if (matrix[r][c] > target) {
                right = m - 1;
            } else if (matrix[r][c] == target) {
                return true;
            } else {
                left = m + 1;
            }
        }
        return false;
    }
}

// time O(log(mn))
// space O(1)
// using binary search and search in a sorted array for specific val