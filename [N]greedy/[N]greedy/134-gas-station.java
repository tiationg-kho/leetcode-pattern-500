class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        for (int g: gas) {
            totalGas += g;
        }
        int totalCost = 0;
        for (int c: cost) {
            totalCost += c;
        }
        if (totalGas < totalCost) {
            return - 1;
        }
        int res = 0;
        int cur = 0;
        for (int i = 0; i < gas.length; i++) {
            cur += gas[i];
            cur -= cost[i];
            if (cur < 0) {
                cur = 0;
                res = i + 1;
            }
        }
        return res;
    }
}

// time O(n)
// space O(1)
// using greedy
/*
1. check it is possible or not
2. traverse and rule out the impossible start stations
*/