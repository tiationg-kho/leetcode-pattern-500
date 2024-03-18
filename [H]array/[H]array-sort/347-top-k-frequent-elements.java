class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> valToFreq = new HashMap<>();
        for (int num: nums) {
            valToFreq.compute(num, (key, v) -> v == null ? 1 : v + 1);
        }
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        for (Map.Entry<Integer, Integer> entry: valToFreq.entrySet()) {
            Integer val = entry.getKey();
            Integer freq = entry.getValue();
            heap.offer(new int[]{freq, val});
            if (heap.size() > k) {
                heap.poll();
            }
        }
        int[] res = new int[heap.size()];
        int i = 0;
        for (int[] element: heap) {
            res[i] = element[1];
            i += 1;
        }
        return res;
    }
}

// time O(n + nlogk)
// space O(n + k), due to hashmap and heap
// using heap and top k problem (based on heap) and min heap and hashmap