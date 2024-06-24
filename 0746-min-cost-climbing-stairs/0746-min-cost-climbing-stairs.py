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
        
        # Time: O(n)
        # Space: O(n)
        
        Since MC[i] depends only on MC[i+1] and MC[i+2],
        we only need to store MC[i+1] and MC[i+2] instead of MC[0, 1, ..., n],
        and in each iteration, we just need to swap move MC[i+1] to MC[i+2]
        and overwrite MC[i+1] with MC[i].
        
        => Space: O(1)
        """
        n = len(cost)
        MC_i1, MC_i2 = cost[n-2], cost[n-1] # initialize MC[n-2] and MC[n-1]
        
        for i in reversed(range(n-2)): # n-3 down to 0
            # calculate new MC[i] and set the prev MC[i+1] to MC[i+2]
            MC_i1, MC_i2 = cost[i] + min(MC_i1, MC_i2), MC_i1
        
        return min(MC_i1, MC_i2)