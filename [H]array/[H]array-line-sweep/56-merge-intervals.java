class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        ArrayList<int[]> res = new ArrayList<>();
        int prevS = intervals[0][0];
        int prevE = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int curS = intervals[i][0];
            int curE = intervals[i][1];
            if (prevE < curS) {
                res.add(new int[]{prevS, prevE});
                prevS = curS;
                prevE = curE;
            } else {
                prevE = Math.max(prevE, curE);
            }
        }
        res.add(new int[]{prevS, prevE});
        return res.toArray(new int[res.size()][2]);
    }
}

// time O(nlogn)
// space O(n), due to output and sort
// using array and line sweep and compare two intervals each round and sort