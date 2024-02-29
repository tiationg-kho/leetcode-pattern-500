class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int oldColor = image[sr][sc];
        if (oldColor == color) {
            return image;
        }
        int rows = image.length;
        int cols = image[0].length;
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Integer> visited = new HashSet<>();
        queue.offer(new int[]{sr, sc});
        visited.add(sr * cols + sc);
        while (!queue.isEmpty()) {
            int[] rc = queue.poll();
            int r = rc[0];
            int c = rc[1];
            image[r][c] = color;
            for (int[] d: new int[][]{{1, 0}, {- 1, 0}, {0, 1}, {0, - 1}}) {
                int nextR = r + d[0];
                int nextC = c + d[1];
                if (0 <= nextR && nextR < rows && 0 <= nextC && nextC < cols && !visited.contains(nextR * cols + nextC) && image[nextR][nextC] == oldColor) {
                    queue.offer(new int[]{nextR, nextC});
                    visited.add(nextR * cols + nextC);
                }
            }
        }
        return image;
    }
}

// time O(RC)
// space O(RC)
// using graph and bfs with single source