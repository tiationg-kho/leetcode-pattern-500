class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] res = new int[rows][cols];

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Integer> visited = new HashSet<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) {
                    queue.offer(new int[]{r, c, 0});
                    visited.add(r * cols + c);
                }
            }
        }
        
        while (!queue.isEmpty()) {
            int[] rcs = queue.poll();
            int r = rcs[0];
            int c = rcs[1];
            int s = rcs[2];
            res[r][c] = s;
            for (int[] nextrc: new int[][]{{r + 1, c}, {r - 1, c}, {r, c + 1}, {r, c - 1}}) {
                int nextr = nextrc[0];
                int nextc = nextrc[1];
                if (0 <= nextr && nextr < rows && 0 <= nextc && nextc < cols && !visited.contains(nextr * cols + nextc)) {
                    queue.offer(new int[]{nextr, nextc, s + 1});
                    visited.add(nextr * cols + nextc);
                }
            }
        }
        return res;
    }
}

// time O(RC)
// space O(RC)
// using graph and bfs with multiple sources