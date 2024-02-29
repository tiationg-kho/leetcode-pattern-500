class Solution {
  public int maxProfit(int[] prices) {
      int res = 0;
      int left = 0;
      for (int right = 0; right < prices.length; right++) {
          if (prices[right] > prices[left]) {
              res = Math.max(res, prices[right] - prices[left]);
          } else {
              left = right;
          }
      }
      return res;
  }
}

// time O(n)
// space O(1)
// using array and two pointers same direction and left ptr to record and greedy