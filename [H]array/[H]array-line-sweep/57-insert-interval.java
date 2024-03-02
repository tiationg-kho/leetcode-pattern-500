class Solution {
  public int[][] insert(int[][] intervals, int[] newInterval) {
      int prevS = newInterval[0];
      int prevE = newInterval[1];
      ArrayList<int[]> res = new ArrayList<>();

      for (int i = 0; i < intervals.length; i++) {
          int curS = intervals[i][0];
          int curE = intervals[i][1];
          if (prevE < curS) {
              res.add(new int[]{prevS, prevE});
              res.addAll(Arrays.asList(Arrays.copyOfRange(intervals, i, intervals.length)));
              return res.toArray(new int[res.size()][2]);
          } else if (prevS > curE) {
              res.add(new int[]{curS, curE});
          } else {
              prevS = Math.min(prevS, curS);
              prevE = Math.max(prevE, curE);
          }
      }
      res.add(new int[]{prevS, prevE});
      return res.toArray(new int[res.size()][2]);
  }
}

// time O(n)
// space O(n), due to output list
// using array and line sweep and compare two intervals each round