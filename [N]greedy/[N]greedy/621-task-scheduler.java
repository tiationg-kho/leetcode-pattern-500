class Solution {
    public int leastInterval(char[] tasks, int n) {
        HashMap<Character, Integer> charToFreq = new HashMap<>();
        for (int i = 0; i < tasks.length; i++) {
            charToFreq.compute(tasks[i], (k, v) -> v == null ? 1 : v + 1);
        }
        int maxFreq = Collections.max(charToFreq.values());
        int maxFreqCount = 0;
        for (Character c: charToFreq.keySet()) {
            if (Objects.equals(charToFreq.get(c), maxFreq)) {
                maxFreqCount += 1;
            }
        }
        return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxFreqCount);
    }
}

// time O(n)
// space O(1), due to task's category
// using greedy and hashmap