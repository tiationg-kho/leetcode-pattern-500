class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        def find(k):
            base = 109
            mod = 10**9+7
            hashval_set = set()
            hashval = 0
            remove_base = (base ** (k - 1)) % mod
            for i, num in enumerate(nums1):
                if i >= k:
                    hashval -= (remove_base * nums1[i - k]) % mod
                hashval = (hashval * base + nums1[i]) % mod
                if i >= k - 1:
                    hashval_set.add(hashval)
            
            hashval = 0
            for i, num in enumerate(nums2):
                if i >= k:
                    hashval -= (remove_base * nums2[i - k]) % mod
                hashval = (hashval * base + nums2[i]) % mod
                if i >= k - 1:
                    if hashval in hashval_set:
                        return True
            return False

        left, right, boundary = 1, len(nums1), 0
        while left <= right:
            m = (left + right) // 2
            if find(m):
                boundary = m
                left = m + 1
            else:
                right = m - 1
        return boundary

# time O((n+m) * log(min(n, m))
# space O(n)
# using string and rabin krap and binary search