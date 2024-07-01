class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Let CC[i] be the fewest number of coins needed to make up `i` amount of money, given the coin denominations. If CC[i] is -1, then that amount cannot be made up by any combination of the coins.
        
        We want to find CC[amount].
        
        Constraint: 0 <= i <= amount
        
        Base Case:
            We can make 0 amount of money with 0 coins, so CC[0] := 0
            For each given denomination i, there exists a coin of that amount, so CC[i] := 1
        """
        coins.sort() # sort coin denominations in ascending order
        CC = [float("inf")] * (amount + 1) # initialize DP array
        
        # Base cases
        CC[0] = 0
        
        while coins and coins[-1] > amount:
            # remove denominations that are invalid
            del coins[-1]
        
        # Generate all combinations possible, caching intermediate results
        for subamt in range(1, amount+1):
            for c in coins:
                diff = subamt - c

                if diff >= 0:
                    CC[subamt] = min(CC[subamt], 1 + CC[diff])
                else:
                    continue

        return CC[amount] if CC[amount] < float("inf") else -1