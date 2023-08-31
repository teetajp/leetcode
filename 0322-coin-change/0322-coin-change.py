class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming problem
        
    # Let c[i] be the minimum number of coins needed to make i amount of money.
    
    # c[i] = min( coins[i - c_j] + 1, for all j < len(coins))
        if amount == 0:
            return 0 # base case 
        
        coins.sort() # smallest to largest
        c = [math.inf for i in range(0, amount+1)]
        # base cases
        c[0] = 0
        max_denom_idx = -1
        for i in range(len(coins)):
            denom = coins[i]
            if denom <= amount:
                c[denom] = 1
                max_denom_idx = i
            else:
                break
        if max_denom_idx == -1:
            return -1
        
        for a in range(1, amount+1):
            # bottom up approach
            for j in range(max_denom_idx, -1, -1):
                if coins[j] <= a and a - coins[j] >= 0:
                    c[a] = min(c[a], c[a - coins[j]] + 1)
                
            
        if c[amount] == math.inf:
            # no viable solution
            return -1 
        return c[amount] # final sol