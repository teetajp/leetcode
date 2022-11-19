class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let n be the number of houses you can rob
        # Let maxLoot(i, j) represent the maximum amount of money you can rob from nums[i...n], given that you choose to rob the house where j is a boolean representing when we have chosen to rob the house (so if j=False, we can rob or not rob the house)
        
        # Recursively we define maxLoot as:
        #   maxLoot(i, 1) = nums[i] + maxLoot(i+2, 0) # since we rob house i, skip house i+1, and look at i+2
        #   maxLoot(i) = 0 when i < 0 or i >= n
        
        # We want to compute maxLoot(0, 0)
        # We have to fill the array from with i <- n down to 0 to satisfy the dependencies
        # Also compute j=1 first before j=0
        
#         n = len(nums)
#         maxLoot = [[0 for i in range(n + 2)] for j in range(2)]
#         for i in range(n-1, -1, -1):
#             maxLoot[1][i] = nums[i] + maxLoot[0][i+2]
#             maxLoot[0][i] = max( maxLoot[1][i], maxLoot[1][i+1] )      
                
#         return maxLoot[0][0]
#         # O(n) time to fill the DP array, O(2n) space for DP memoization array
    
        maxLoot = (0, 0) # first index stores the max loot from the i-2th iteration, and second index stores current iteration's max loot
        for loot in nums:
            maxLoot = ( maxLoot[1], max(maxLoot[1], loot + maxLoot[0]) )
        return maxLoot[1]
            