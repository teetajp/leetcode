class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Let minCost[i] be the cost of climbing the stairs from the ith step till the top of stairs
        # Our recursive formula is defined as:
        #   minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])                     if i < len(cost)
        #   minCost[i] = 0                                                             if i >= len(cost)
        minCost = [0 for i in range(len(cost) + 2)] # 2 placeholder value to represent when i >= len(cost) - 1
        
        for i in range(len(cost)-1, -1, -1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        
        return min(minCost[0], minCost[1])