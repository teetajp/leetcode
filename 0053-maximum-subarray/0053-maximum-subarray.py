class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy sliding window?
        max_sum = float("-inf")
        cur_sum = 0
        l, r = 0, 0
        for r in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
                l = r
                
            cur_sum += nums[r]
            
            max_sum = max(max_sum, cur_sum)
            
        return max_sum