class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> charToWeight = new HashMap<>();
        charToWeight.put('I', 1);
        charToWeight.put('V', 5);
        charToWeight.put('X', 10);
        charToWeight.put('L', 50);
        charToWeight.put('C', 100);
        charToWeight.put('D', 500);
        charToWeight.put('M', 1000);
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            int w = charToWeight.get(c);
            if (i + 1 < s.length() && charToWeight.get(s.charAt(i + 1)) > w) {
                res -= w;
            } else {
                res += w;
            }
        }
        return res;
    }
}

// time O(n), due to traverse, n is the length of input string
// space O(1), hashmap's size is O(7)
// using hashmap and store val