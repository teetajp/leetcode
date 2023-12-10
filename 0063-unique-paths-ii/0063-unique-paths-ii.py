class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recurrence relation:
        # let DP[i][j] be the number of unique paths from (0, 0) to (i, j).
        # We want to find DP[m-1][n-1].
        # Base case:
        #   DP[0][0] = 1 if grid[0][0] == 0 else 0
        #   DP[i][0] = grid[i-1][j]
        #   DP[0][j] = grid[0][j-1]
        # Recursive case:
        #   DP[i][j] = DP[i-1][j] + DP[i][j-1]
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        
        for i in range(1, max(m, n)):
            if i < m and obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            if i < n and obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]