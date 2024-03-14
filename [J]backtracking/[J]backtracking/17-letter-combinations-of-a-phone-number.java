class Solution {

    HashMap<Character, ArrayList<Character>> map;
    List<String> res;

    public List<String> letterCombinations(String digits) {
        map = new HashMap<>();
        int cur = 0;
        for (int i = 2; i < 10; i++) {
            char c = (char) (i + '0');
            int total = 3;
            if (i == 7 || i == 9) {
                total += 1;
            }
            for (int j = 0; j < total; j++) {
                map.computeIfAbsent(c, k -> new ArrayList<>()).add((char) (cur + 'a'));
                cur += 1;
            }
        }
        res = new ArrayList<>();
        if (digits.length() > 0) {
            dfs(digits, new StringBuffer(), 0);
        }
        return res;
    }

    public void dfs(String digits, StringBuffer sb, int idx) {
        if (idx == digits.length()) {
            res.add(sb.toString());
            return;
        }
        for (int i = 0; i < map.get(digits.charAt(idx)).size(); i++) {
            Character c = map.get(digits.charAt(idx)).get(i);
            sb.append(c);
            dfs(digits, sb, idx + 1);
            sb.deleteCharAt(sb.length() - 1);
        }
        return;
    }
}

// time O(4**n), n is the length of digits
// space O(n), due to recursion stack, output is O(4**n)
// using dfs and backtracking and backtracking with constraints