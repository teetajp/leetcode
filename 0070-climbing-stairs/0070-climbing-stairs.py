class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def stepCounts(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            return stepCounts(i-1) + stepCounts(i-2)
        return stepCounts(n)