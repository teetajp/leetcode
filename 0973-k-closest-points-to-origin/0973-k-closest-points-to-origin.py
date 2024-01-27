import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # initialize a max heap of size k
        # we will iterate through the list of points:
        #   - calculate the Euclidean distance between the origin and each point_i
        #   - if heap is not yet size k, push to it
        #   - if heap is size k, compare against top of heap
        #       - if point is smaller than the top of the heap,
        #           then pop the top elem and push the point onto the max heap
        #       - if point is larger than top of the heap, do nothing
        def distToOrigin(x: int, y: int) -> int:
            # since sqrt((x-0)^2) == sqrt(x^2) == abs(x), we can just use that as well
            # return abs(x) + abs(y)
            return sqrt(x**2 + y**2)
        
        maxHeap = [(-distToOrigin(*points[i]), points[i]) for i in range(k)] 
        heapq.heapify(maxHeap) 
        
        for i in range(k, len(points)):
            # iterate over the remaining elements: (k+1)th to nth elem
            cur_dist = distToOrigin(*points[i])
            if cur_dist < -maxHeap[0][0]:
                # smaller distance than the current min kth in heap, replace it
                heapq.heappushpop(maxHeap, (-cur_dist, points[i]))
        
        return [dist_point[1] for dist_point in maxHeap]