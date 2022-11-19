class Solution:
    def rob(self, nums: List[int]) -> int:
        # To maximize amount we can rob, we should rob one house in every pair of houses
        # There are two configurations (let 1 represent a house we plan to rob and 0 represent a house we don't plan to rob):
        # [1, 0] ... => we rob the first house in the pair
        # [0, 1] ... => we rob the second house in the pair
        # Edge case:
        # - odd number of houses: [1, 3, 2]
        #   - in this case, we can choose can only choose a house in either the pair (1, 3) or (3, 2) to rob
        # Let's look at when n >= 4:
        # For every two pairs (h_i, h_i+1) and (h_i+2, h_i+3), where the subscript represnets houses in order
        # We cannot have the configurations:
        # - (0, 1) (1, 0) where we rob the second house in the first pair and the first house in the second pair
        # For the config (1, 0) (0, 1) where we rob the first house in the first pair and the second house in the second pair
        #   We would be forced to not round the next house, only allow (0, 0) or (0, 1)
        
        # Let n be the number of houses you can rob
        # Let maxLoot(i, j) represent the maximum amount of money you can rob from nums[i...n], given that you choose to rob the house when j = 1 (have a choice to rob or not rob when j = 0)
        # Recursively,
        #   maxLoot(i, 0) = max( maxLoot(i, 1), maxLoot(i+1, 1) )
        #   maxLoot(i, 1) = nums[i] + maxLoot(i+2, 0) # since we rob house i, skip house i+1, and look at i+2
        #   maxLoot(i) = 0 when i < 0 or i >= n
        
        # We want to compute maxLoot(0, 0)
        # We have to fill the array from with i <- n down to 0 to satisfy the dependencies
        # Also compute j=1 first before j=0
        @lru_cache(None)
        def maxLoot(i: int, willRob: bool) -> int:
            if i >= len(nums):
                return 0
            if willRob:
                return nums[i] + maxLoot(i+2, False)
            return max( maxLoot(i, 1), maxLoot(i+1, 1) )
        
        return maxLoot(0, 0)
            
            