from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sums = Counter()
        for val in sorted(nums): # O(nlogn) for sort + O(n) to insert to dict
            sums[val] += val
        
        k, keys = len(sums), list(sums.keys())
        
        if k == 1:
            return sums[keys[0]]
        
        dp = [0] * (k+1)
        dp[0] = sums[keys[0]]
        
        dp[1] = max(dp[0], sums[keys[1]]) if keys[1] - keys[0] == 1 else sums[keys[1]] + dp[0]
        for i in range(2, k):
            dp[i] = max(sums[keys[i]] + dp[i-2], dp[i-1]) if keys[i] - keys[i-1] == 1 else sums[keys[i]] + dp[i-1]
        
        return dp[k-1]