class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Let n = len(cost) >= 2be the top floor.
        Let MC[i] be the minimum cost of climbing from the i-th step to the n-th step/floor.
        
        Final answer: min(MC[0], MC[1])
        
        Base Case:
        - MC[n] := 0
        - MC[n-1] := cost[n-1]
        - MC[n-2] := cost[n-2]
        
        Recursive Case:
        - For 0 <= i <= n-3,
            MC[i] := cost[i] + min(MC[i+1], MC[i+2])
        
        Order:
        - fill linearly from MC[n] down to MC[0]
        """
        n = len(cost)
        MC = [0] * n # [0, 1, ..., n-2, n-1]
        MC[n-1], MC[n-2] = cost[n-1], cost[n-2]
        
        for i in reversed(range(n-2)): # n-3 down to 0
            MC[i] = cost[i] + min(MC[i+1], MC[i+2])
        
        return min(MC[0], MC[1])
    
    
    # Time: O(n)
    # Space: O(n)