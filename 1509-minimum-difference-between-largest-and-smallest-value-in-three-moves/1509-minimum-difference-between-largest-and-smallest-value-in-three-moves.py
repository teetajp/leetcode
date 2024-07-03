import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        # For n <= 3, set all elems to same val
        # For n == 4, then the only elem is both the min and the max
        
        Since we only need to get largest and smallest 4 values (3 for change, 1 to guarantee a value to compare)
        
        We can sort in O(n + n log 4) = O(n) time
        
        Then we can bruteforce all (2^3 = 8) combinations of the values to pop
        
        Time: O(n)
        Space: O(1) disregarding `nums` input array (to further optimize, pop nums while updating heap)
        """
        if len(nums) <= 4:
            return 0
        
        minElems, maxElems = [], []
        
        while nums:
            i = nums.pop()
            
            if len(minElems) < 4:
                heapq.heappush(minElems, -i)
            elif i < -minElems[0]:
                heapq.heappushpop(minElems, -i)
            
            if len(maxElems) < 4:
                heapq.heappush(maxElems, i)
            elif i > maxElems[0]:
                heapq.heappushpop(maxElems, i)
        
        # bruteforce all 2^3 choices
        minElems = [-i for i in minElems]
        heapq.heapify(minElems)
        heapq.heapify(maxElems)
        res = float("inf")

        while maxElems and minElems:
            res = min(res, heapq.heappop(maxElems) - heapq.heappop(minElems))
            
        return res