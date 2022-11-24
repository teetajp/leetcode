class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    # Let MaxSum(i) be the maximum sum of any subarray in the nums array from index 0 to index i.
    #
    # MaxSum(i) = { 0                                       if i < 0 or i >= n
    #             { max( MaxSum(i-1) + max(0, nums[i]),     else    # previous subarray sum and include current value if positive 
    #                  nums[i]                     )                # new subarray starting at index i
    #       
    # We want to compute the maximum MaxSum(i) for 0 <= i < n
        n, global_max = len(nums), nums[0]
        
        def MaxSum(i: int) -> int:
            if i < 0 or i >= n:
                return 0
            curr_max = nums[i] + max(0, MaxSum(i-1))
            nonlocal global_max
            global_max = max(global_max, curr_max)
            return curr_max
        
        MaxSum(n-1)
            
        return global_max