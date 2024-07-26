class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        
        
        dp[0][j] = 1
        dp[i][0] = 1
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        
        dp = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j] # left + up
                
        return dp[n-1]