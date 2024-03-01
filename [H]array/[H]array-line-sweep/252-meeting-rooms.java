class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals.length == 0) {
            return true;
        }
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        int prevE = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int curS = intervals[i][0];
            int curE = intervals[i][1];
            if (prevE > curS) {
                return false;
            }
            prevE = Math.max(prevE, curE);
        }
        return true;
    }
}

// time O(nlogn)
// space O(1), or consider sort's cost
// using array and line sweep and compare two intervals each round