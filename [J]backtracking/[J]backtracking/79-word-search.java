class Solution {
    char[][] board;
    String word;
    int rows;
    int cols;

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word;
        rows = board.length;
        cols = board[0].length;

        HashMap<Character, Integer> charToFreq = new HashMap<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                charToFreq.compute(board[r][c], (k, v) -> v == null ? 1 : v + 1);
            }
        }
        for (int i = 0; i < word.length(); i++) {
            Character c = word.charAt(i);
            if (!charToFreq.containsKey(c)) {
                return false;
            }
            charToFreq.put(c, charToFreq.get(c) - 1);
            if (Objects.equals(charToFreq.get(c), 0)) {
                charToFreq.remove(c);
            }
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                HashSet<Integer> visited = new HashSet<>();
                if (dfs(r, c, 0, visited) == true) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(int r, int c, int idx, HashSet<Integer> visited) {
        if (0 > r || r >= rows || 0 > c || c >= cols || visited.contains(r * cols + c) || board[r][c] != word.charAt(idx)) {
            return false;
        }
        if (idx == word.length() - 1) {
            return true;
        }
        visited.add(r * cols + c);
        for (int[] nextrc: new int[][]{{r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}}) {
            if (dfs(nextrc[0], nextrc[1], idx + 1, visited) == true) {
                return true;
            }
        }
        visited.remove(r * cols + c);
        return false;

    }
}

// time O(RC * 3**L)
// space O(RC), due to hashset
// using dfs and backtracking and backtracking with constraints and pruning