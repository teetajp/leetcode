class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        maxLIS: list[int] = [1] * len(nums) # initialize DP array; lower bound of all answer is 1 (subseq with just the element)
        res = 1
        for i in range(1, len(nums)):
            
            # length of maxLIS before iteration i, where sequence was lower in value
            maxLIS[i] = 1 + max((maxLIS[j] for j in reversed(range(0, i)) if nums[j] < nums[i]), default=0)
            res = max(res, maxLIS[i])
        
        
        return res
        