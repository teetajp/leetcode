class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        
        
        dp[0][j] = 1
        dp[i][0] = 1
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        to further optimize, get the min of (m, n)
        """
        dp = [1] * min(m, n)

        for _ in range(1, max(m, n)):
            for i in range(1, min(m, n)):
                dp[i] = dp[i-1] + dp[i] # left + up
                    
        return dp[min(m, n)-1]