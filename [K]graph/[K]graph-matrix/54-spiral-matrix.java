class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int d = 0;
        int r = 0;
        int c = 0;
        int[][] directions = new int[][]{{0, 1}, {1, 0}, {0, - 1}, {- 1, 0}};
        HashSet<Integer> visited = new HashSet<>();
        List<Integer> res = new ArrayList<>();
        while (res.size() < rows * cols) {
            res.add(matrix[r][c]);
            visited.add(r * cols + c);
            int nextR = r + directions[d][0];
            int nextC = c + directions[d][1];
            if (0 > nextR || nextR >= rows || 0 > nextC || nextC >= cols || visited.contains(nextR * cols + nextC)) {
                d = (d + 1) % directions.length;
                nextR = r + directions[d][0];
                nextC = c + directions[d][1];
            }
            r = nextR;
            c = nextC;
        }
        return res;
    }
}

// time O(RC)
// space O(RC)
// using graph and matrix and hashset