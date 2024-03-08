class Solution {
    public int numIslands(char[][] grid) {
        int res = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        HashSet<Integer> visited = new HashSet<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (visited.contains(r * cols + c) || grid[r][c] == '0') {
                    continue;
                }
                ArrayDeque<int[]> queue = new ArrayDeque<>();
                queue.offer(new int[]{r, c});
                visited.add(r * cols + c);
                res += 1;
                while (!queue.isEmpty()) {
                    int[] rc = queue.poll();
                    int cur_r = rc[0];
                    int cur_c = rc[1];
                    for (int[] nextrc: new int[][]{{cur_r+1, cur_c}, {cur_r-1, cur_c}, {cur_r, cur_c+1}, {cur_r, cur_c-1}}) {
                        int next_r = nextrc[0];
                        int next_c = nextrc[1];
                        if (0 <= next_r && next_r < rows && 0 <= next_c && next_c < cols && !visited.contains(next_r * cols + next_c) && grid[next_r][next_c] == '1') {
                            queue.offer(new int[]{next_r, next_c});
                            visited.add(next_r * cols + next_c);
                        }
                    }
                }
            }
        }
        return res;
    }
}

// time O(RC)
// space O(RC)
// using graph and bfs with single source