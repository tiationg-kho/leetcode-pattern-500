class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr + [0]
        stack = []
        res = 0
        for i in range(len(arr)):
            while stack and arr[stack[- 1]] > arr[i]:
                idx = stack.pop()
                left_bound = stack[- 1]
                right_bound = i
                left_choices = idx - left_bound
                right_choices = i - idx
                res += left_choices * right_choices * arr[idx]
            stack.append(i)
        return res % (10**9+7)
                   
# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider two side’s relationship)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        smaller_in_right = [len(arr) for _ in range(len(arr))]
        stack = []
        for i, num in enumerate(arr):
            while stack and arr[stack[- 1]] >= num:
                idx = stack.pop()
                smaller_in_right[idx] = i
            stack.append(i)

        smaller_in_left = [- 1 for _ in range(len(arr))]
        stack = []
        for i in range(len(arr) - 1, - 1, - 1):
            while stack and arr[stack[- 1]] > arr[i]:
                idx = stack.pop()
                smaller_in_left[idx] = i
            stack.append(i)

        res = 0
        for i in range(len(arr)):
            left_bound = smaller_in_left[i]
            right_bound = smaller_in_right[i]
            left_choices = i - left_bound
            right_choices = right_bound - i
            res += left_choices * right_choices * arr[i]
        return res % (10**9+7)

# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider two side’s relationship)