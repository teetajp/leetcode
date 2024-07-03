import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            # For n <= 3, set all elems to same val
            # For n == 4, then the only elem is both the min and the max
            return 0
        
        """
        Since we only need to get largest and smallest 4 values (3 for change, 1 to guarantee a value to compare)
        
        We can sort in O(n + n log 4) = O(n) time
        
        Then we can bruteforce all (2^3 = 8) combinations of the values to pop
        
        Time: O(n)
        Space: O(1) disregarding `nums` input array (to further optimize, pop nums while updating heap)
        """
        
        minElems = heapq.nsmallest(4, nums)
        maxElems = heapq.nlargest(4, nums)
        
        # bruteforce all 2^3 choices
        return min(maxElems[-1-i] - minElems[i] for i in range(0, 4))