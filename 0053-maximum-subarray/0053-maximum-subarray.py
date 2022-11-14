class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # cur_max is the max subarray sum ending at i (dynamically choosing whether to reset and start new subarray at current index or to include current and append to previous subarray)
        # max_over_i is the maximum sum we have seen till now (after i^th iterations)
        cur_max, max_over_i = 0, -inf
        for x in nums:
            cur_max = max(x, cur_max + x)
            max_over_i = max(max_over_i, cur_max)
        return max_over_i
    
    # O(n) time
    # O(1) space