class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        
        
        dp[0][j] = 1
        dp[i][0] = 1
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        to further optimize, get the min of (m, n)
        """
        if n <= m:
            dp = [1] * n

            for _ in range(1, m):
                for j in range(1, n):
                    dp[j] = dp[j-1] + dp[j] # left + up
                    
            return dp[n-1]
        else:
            dp = [1] * m
            
            for _ in range(1, n):
                for i in range(1, m):
                    dp[i] = dp[i-1] + dp[i] # left + up
            
                
            return dp[m-1]