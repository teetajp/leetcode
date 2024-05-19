class MedianFinder:

    def __init__(self):
        self.minHeap = [] # top 50%
        self.maxHeap = [] # bottom 50%

    def addNum(self, num: int) -> None:
        if len(self.minHeap) >= len(self.maxHeap):
            # bias towards minHeap if uneven counts
            displacedNum = heapq.heappushpop(self.minHeap, num)
            heapq.heappush(self.maxHeap, -displacedNum)
        else:
            displacedNum = heapq.heappushpop(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -displacedNum)
        
        

    def findMedian(self) -> float:
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