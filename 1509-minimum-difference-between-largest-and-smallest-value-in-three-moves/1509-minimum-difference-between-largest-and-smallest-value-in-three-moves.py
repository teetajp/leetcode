import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            # can change up to 3 vals, and n == 4, then the only elem is both min and max
            return 0
        
        """
        Since we only need to get largest and smallest 4 values (3 for change, 1 to guarantee a value to compare)
        
        We can sort in O(n + n log 4) = O(n)
        
        Then we can bruteforce all (2^3 = 8) combinations of the values to pop
        """
        # nums.sort()
        print(nums)
        
        minElems = heapq.nsmallest(4, nums)
        maxElems = heapq.nlargest(4, nums)
        # bruteforce all 2^3 choices
        # res = nums[-1] - nums[0]
        # for i in range(0, 4):
        #     l, r = nums[i], nums[-4+i]
        #     res = min(res, r - l)
        res = maxElems[0] - minElems[0]
        
        for i in range(0, 4):
            res = min(res, maxElems[-1-i] - minElems[i])
            
        return res