class MedianFinder:

    def __init__(self):
        self.minHeap = [] # top 50%
        self.maxHeap = [] # bottom 50%
        # bias towards minHeap if uneven counts
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) >= len(self.maxHeap):
            displacedNum = heapq.heappushpop(self.minHeap, num)
            heapq.heappush(self.maxHeap, -displacedNum)
        else:
            displacedNum = heapq.heappushpop(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -displacedNum)
        

    def findMedian(self) -> float:
        # assuming there is always at least one element in one of the heaps
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0] 
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0] 
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()