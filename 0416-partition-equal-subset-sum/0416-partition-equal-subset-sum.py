from collections import defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Sum must be even number, since we are using integers.
        Even if we sum is even, we may not be able to partition if we elements unevenly weighted, such as if there is only one element and it is even.
        
        Each element can belong to one of two groups.
        
        Consider nums be to be sorted.
        
        Brute force: try all O(2^n) combinations.
        
        We want the sum of each partition to be equal, or equivalently, the sum of one of the partition to be sum(nums) / 2, since the other partition must be equal since we checked for the odd case earlier.
        
        Rephrased problem statement: can we choose a subset of nums such that the sum of that subset == sum(nums) // 2?
        
        Can check if at a given index with a certain sum, if has already been checked, then we know we cant partition it, and return early.
        
        Let DP[i][target] be whether we can choose a subset of nums beteween nums[i:n] whose sum == target.
        
        Base Case:
            DP[n-1][nums[n-1]] = True # when this partition needs `nums[n-1]` more sum val
            DP[n-1][0] = True # when this partition has enough sum alr, but the other needs more
            else DP[n-1][target] = False
            # this implies that if there is only one elem, then it is only true if nums[n-1] == 0
            
        Recursive Case:
            DP[i][target] = DP[i+1][target - nums[i]] or DP[i+1][target]
            # add this val to current partition sum OR add this val to other partition sum
            
        Final Answer:
            DP[0][sum(nums) / 2]
                
         Use a set to dynamically track the possible sums we can achieve.
                
        Runtime: O(n * target)
        Space: O(target)???
        """
        total_sum = sum(nums)
        
        # If the total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Create a DP array with target + 1 length
        dp = [False] * (target + 1)
        dp[0] = True  # We can always achieve a sum of 0 by taking no elements
        
        for num in nums:
            # Traverse the dp array backwards to avoid overwriting results we need to use in this iteration
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]