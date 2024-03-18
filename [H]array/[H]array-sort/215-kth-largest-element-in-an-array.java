class Solution {
    public int findKthLargest(int[] nums, int k) {

        HashMap<Integer, Integer> valToFreq = new HashMap<>();
        for (int num: nums) {
            valToFreq.compute(num, (key, v) -> v == null ? 1 : v + 1);
        }
        int maxFreq = Collections.max(valToFreq.values());
        if (maxFreq > k && maxFreq > nums.length - k) {
            for (Integer key: valToFreq.keySet()) {
                if (Objects.equals(valToFreq.get(key), maxFreq)) {
                    return key;
                }
            }
        }

        int left = 0;
        int right = nums.length - 1;
        int idx = 0;
        while (left <= right) {
            idx = quickSelect(nums, left, right);
            if (idx == nums.length - k) {
                break;
            } else if (idx > nums.length - k) {
                right = idx - 1;
            } else {
                left = idx + 1;
            }
        }
        return nums[idx];
    }

    public int quickSelect(int[] nums, int left, int right) {
        Random random = new Random();
        int pivotIdx = random.nextInt(right - left + 1) + left;
        int pivotVal = nums[pivotIdx];
        swap(nums, pivotIdx, right);
        int partitionIdx = left;
        for (int i = left; i < right; i++) {
            if (nums[i] < pivotVal) {
                swap(nums, partitionIdx, i);
                partitionIdx += 1;
            }
        }
        swap(nums, partitionIdx, right);
        return partitionIdx;
    }

    public void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
        return;
    }
}

// time O(n**2) in worst, O(n) in average (notice that quick sort is O(nlogn) in average)
// space O(n), due to hashmap
// using array and sort and top k problem (based on sort) and quick select and prune