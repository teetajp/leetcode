class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[0][j] = 1
        dp[i][0] = 1
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        to further optimize, get the min of (m, n)
        """
        minDim, maxDim = min(m, n), max(m, n)
        dp = [1] * minDim

        for _ in range(1, maxDim):
            for i in range(1, minDim):
                dp[i] += dp[i-1] # left + up
                    
        return dp[minDim-1]