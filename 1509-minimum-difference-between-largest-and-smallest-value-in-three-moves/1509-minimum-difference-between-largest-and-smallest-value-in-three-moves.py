class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 4:
            # can change up to 3 vals, and n == 4, then the only elem is both min and max
            return 0
        
        """
        Since we only need to get largest and smallest 4 values (3 for change, 1 to guarantee a value to compare)
        
        We can sort in O(n + n log 4) = O(n)
        
        Then we can bruteforce all (2^3 = 8) combinations of the values to pop
        """
#         minHeap = []
#         maxHeap = []
        
#         # find top/bottom 4 vals and discard the rest
#         while nums:
#             i = nums.pop()
            
#             if len(minHeap) < 4:
#                 heapq.heappush(minHeap, i)
#                 continue
#             elif i < minHeap[0]:
#                 # found new min when heap is full
#                 heapq.heapreplace(minHeap, i)
#                 continue
            
#             if len(maxHeap) < 4:
#                 heapq.heappush(maxHeap, -i)
#                 continue
#             elif -i < maxHeap[0]:
#                 # found new max when heap is full
#                 heapq.heapreplace(maxHeap, -i)
#                 continue

        nums.sort()
        print(nums)
        
        # bruteforce all 2^3 choices
        res = nums[-1] - nums[0]
        for i in range(0, 4):
            l, r = nums[i], nums[-4+i]
            print(r, l)
            res = min(res, r - l)
        # [0, 1, 5, 10, 14]
        return res