class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])        if i < len(cost)
        # 0                                                             if i >= len(cost)
        n = len(cost)
        minCost = [0 for i in range(n + 2)] # 2 placeholder value to represent when i >= len(cost) - 1
        
        for i in range(n-1, -1, -1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        
        return min(minCost[0], minCost[1])