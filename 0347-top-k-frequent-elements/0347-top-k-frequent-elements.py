import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a min heap
        # iterate over the nums array O(n)
        # OR use hashmap to keep a count of each freq, then iterate over the entries while using a min heap of size k
        
        # Time Complexity: O(n) to iterate and count freq, O(k) + O((n-k)*logk) worst case for heao => O(n + k + (n-k)*log(k))
        # Space Complexity: O(k) for hashmap, O(k) for minheap => total O(k) if excluding input array
        freq = {}
        for n in nums:
            freq[n] = freq[n] + 1 if n in freq else 1
        
        minHeap = []
        for idx, n in enumerate(freq):
            if idx < k:
                minHeap.append((freq[n], n))
                if len(minHeap) == k:
                    heapq.heapify(minHeap)
            else:
                if freq[n] > minHeap[0][0]:
                    heapq.heappushpop(minHeap, (freq[n], n))
        
        return [key for count, key in minHeap] 