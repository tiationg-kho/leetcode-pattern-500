class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int fresh = 0;
        int rotten = 0;
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Integer> visited = new HashSet<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    fresh += 1;
                }
                else if (grid[r][c] == 2) {
                    rotten += 1;
                    queue.offer(new int[]{r, c, 0});
                    visited.add(r * cols + c);
                }
            }
        }
        if (fresh == 0) {
            return 0;
        }
        if (rotten == 0) {
            return - 1;
        }
        int res = 0;
        while (!queue.isEmpty()) {
            int[] rc = queue.poll();
            int r = rc[0];
            int c = rc[1];
            int step = rc[2];
            res = step;
            if (grid[r][c] == 1) {
                fresh -= 1;
            }
            for (int[] nextrc: new int[][]{{r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}}) {
                int next_r = nextrc[0];
                int next_c = nextrc[1];
                if (0 <= next_r && next_r < rows && 0 <= next_c && next_c < cols && !visited.contains(next_r * cols + next_c) && grid[next_r][next_c] == 1) {
                    queue.offer(new int[]{next_r, next_c, step + 1});
                    visited.add(next_r * cols + next_c);
                }
            }
        }
        return fresh == 0 ? res : - 1;
    }
}

// time O(RC)
// space O(RC)
// using graph and bfs with multiple sources