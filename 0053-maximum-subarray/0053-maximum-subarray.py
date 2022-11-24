class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    # Let MaxSum(i) be the maximum sum of any subarray in the nums array from index 0 to index i.
    #
    # MaxSum(i) = { 0                                       if i < 0 or i >= n
    #             { max( MaxSum(i-1) + max(0, nums[i]),     else    # previous subarray sum and include current value if positive 
    #                  nums[i]                     )                # new subarray starting at index i
    #       
    # We want to compute the maximum MaxSum(i) for 0 <= i < n
        n, prevSum, global_max = len(nums), nums[0], nums[0]
        
        for i in range(1, n):
            prevSum = nums[i] + max(0, prevSum)
            global_max = max(prevSum, global_max)
            
        return global_max
    # O(n) time
    # O(1) space