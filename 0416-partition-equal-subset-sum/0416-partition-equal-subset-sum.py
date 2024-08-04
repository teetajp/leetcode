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
        
        new problem statement: can we choose a subset of nums such that the sum of that subset == sum(nums) // 2?
        
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
        
        Evaluation Order:
            iterate from i := n-1 -> 0
                target_{i} := { target_{i+1} - nums[i+1], target_{i+1}   }
                OR target_{i} = argmax(dp[i+1]) ??
                
        Runtime: O(n)???
        Space: O(n * range(nums))???
        """
        target, rem = divmod(sum(nums), 2)

        if rem != 0 or (len(nums) == 1 and nums[0] != 0):
            return False
        elif target == 0:
            return True
        
        # base case
        validSums = set([0, nums[-1]])
        
        for i in range(len(nums)-2, -1, -1):
            newSums = set()
            
            for j in validSums:
                newSums.add(nums[i] + j)
                
            newSums.add(nums[i])
            validSums.update(newSums)
            
            if target in validSums:
                # found answer, return early
                return True
        
        return False # never found a valid answer