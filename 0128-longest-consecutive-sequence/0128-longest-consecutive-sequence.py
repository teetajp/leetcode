class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sliding window, must be increasing
        if len(nums) == 0:
            return 0
        
        nums.sort()
        max_cnt, cur_cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                # skip duplicates
                continue
            if nums[i-1] == nums[i] - 1:
                cur_cnt += 1
                max_cnt = max(max_cnt, cur_cnt)
            else:
                # if not consecutive, then reset count
                cur_cnt = 1
                
                
        return max_cnt