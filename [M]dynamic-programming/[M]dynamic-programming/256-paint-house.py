class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red = 0
        blue = 0
        green = 0
        for r, b, g in costs:
            red, blue, green = min(blue + r, green + r), min(red + b, green + b), min(red + g, blue + g)
        return min(red, blue, green)
    
# time O(n)
# space O(1)
# using dynamic programming and linear sequence