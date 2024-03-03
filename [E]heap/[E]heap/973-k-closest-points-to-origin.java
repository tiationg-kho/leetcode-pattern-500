class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        int[][] res = new int[k][2];
        for (int[] p: points) {
            heap.offer(new int[]{p[0] * p[0] + p[1] * p[1], p[0], p[1]});
            if (heap.size() > k) {
                heap.poll();
            }
        }
        while (!heap.isEmpty()) {
            int idx = heap.size() - 1;
            int[] p = heap.poll();
            res[idx][0] = p[1];
            res[idx][1] = p[2];
        }
        return res;
    }
}

// time O(nlogk)
// space O(k)
// using heap and top k problem (based on heap) and max heap