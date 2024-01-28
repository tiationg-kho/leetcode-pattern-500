class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        val_idx = {}
        for i, num in enumerate(nums1):
            val_idx[num] = i

        res = [- 1 for _ in range(len(nums1))]
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[- 1]] < nums2[i]:
                idx = stack.pop()
                if nums2[idx] in val_idx:
                    res[val_idx[nums2[idx]]] = nums2[i]
            stack.append(i)
        return res
    
# time O(n)
# space O(n), due to stack and hashmap
# using stack and queue and montonic and monotonic stack (consider one side’s relationship) and hashmap