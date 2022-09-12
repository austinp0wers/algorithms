class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        dpCache = [0] * (n+1)
        dpCache[1] = 1
        dpCache[2] = 2
        for i in range(3, n+1):
            dpCache[i] = dpCache[i-1] + dpCache[i-2]
        return dpCache[n]
        