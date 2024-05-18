import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            
        maxHeap = [(-k, v) for k, v in counts.items()]
        heapq.heapify(maxHeap)
        
        while k > 0:
            num_val, num_count = heapq.heappop(maxHeap)
            k -= min(k, num_count)
        
        return -num_val
    
    # runtime: O(n + k log n)