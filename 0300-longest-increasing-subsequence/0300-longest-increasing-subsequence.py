class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Let LIS[i] be the length of the longest strictly increasing subsequence starting at and including nums[i], ending at nums[n-1].

        LIS[n-1] = 1
        LIS[i] = max { 1 or LIS[i]                , if i+1 > n-1
                     { LIS[i+j] + 1  , if nums[i] < nums[i+j], for i+j <= n-1
        """
        n = len(nums)
        if n == 0: return 0
        
        lis = [1] * n
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        
        return max(lis)