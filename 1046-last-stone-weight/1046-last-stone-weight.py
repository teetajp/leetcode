import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1 # turn into negative for use in the the maxHeap
        heapq.heapify(stones) # O(n)
        
        while len(stones) > 1:
            y = heapq.heappop(stones) # heavier than x
            x = heapq.heappop(stones)
            
            smash_result = y - x # ex: -4 - -3 = -1
            
            if smash_result < 0:
                heapq.heappush(stones, smash_result)
                
        return 0 if not stones else -stones[0]