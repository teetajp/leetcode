class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Cases:
        - 0
        - neg
        - pos
        
        
        let DP[i] be the max subarray product between index 0 and i, including the current element
        
        use mins array as well?
        
        if nums[i] == 0: dp[i] = max(dp_max[i-1], 0)
        if nums[i] > 0: dp[i] = max(dp_max[i-1] * nums[i], nums[i])
        if nums[i] < 0: dp[i] = max(dp_max[i-1], dp_min[i-1] * nums[i], nums[i])
        
        if nums[i] == 0: dp[i] = min(dp_min[i-1], 0)
        if nums[i] > 0: dp[i] = min(dp_min[i-1] * nums[i], nums[i])
        if nums[i] < 0: dp[i] = min(dp_max[i-1] * nums[i], nums[i])
        """
        res = max(nums)
        maxProd, minProd = 1, 1
        
        for i in nums:
            if i == 0:
                maxProd = minProd = 1
                continue

            tmp = i, minProd * i, maxProd *i
            maxProd, minProd = max(tmp), min(tmp)
                
            res = max(res, maxProd, minProd)
            
            
        return res