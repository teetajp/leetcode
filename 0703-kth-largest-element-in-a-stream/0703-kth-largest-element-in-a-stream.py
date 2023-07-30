import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # first method: heapify first k elem into minHeap then heappush/pop
        #   - O( k + (n - k)log(k) ) => O(k + n*log(k))
            
        # second method: heapify nums into maxHeap then extract top k elems
        #   - O( n + k*log(n) )
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums) # O(n)
        self.k = k
        self.minHeap = []
        for _ in range(min(k, len(nums))):
            # add k largest elements in maxHeap into minHeap
            heapq.heappush(self.minHeap, -heapq.heappop(nums))
        
    def add(self, val: int) -> int:
        # nums.append(val)
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)