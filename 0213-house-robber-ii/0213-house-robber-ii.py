class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Same as LC 198 House Robber I
        
        Let MM[i][j] be the maximum money earnable starting at house j till the end of last house if we rob (i=1) or skip (i=0) this house.
        
        Final answer: max(MM[1][1], MM[1][0])
        
        Base Case:
        - MM[n, 1] := nums[n]
        - MM[n, 0] := 0

        Recursive Case:
        - For 0 <= i <= n-1,
            MM[i, 0] := max(MM[i+1, 0], MM[i+1, 1]) # can rob or skip next house
            MM[i, 1] := nums[i] + MM[i+1, 0] # can't rob next house
            
        # XXX: can optimize this and make it 1D?
        
        Fill Order:
        - iterate i from n down to 0
            - iterate j = 0 before j = 1
            
        Two passes:
            To calculate MM[1][0], where we rob the first house,
                we exclude nums[n-1] from our calculation.
            To calculate MM[0][0], we may include nums[n-1] in our calculations.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        MM_skip2, MM_rob2 = 0, nums.pop()
        MM_skip1, MM_rob1 = 0, nums.pop()
        MM_skip2, MM_rob2 = max(MM_skip2, MM_rob2), MM_skip2 + MM_rob1
        
        n -= 2
        
        while nums:
            reward = nums.pop()
            n -= 1
            
            if n >= 1:
                MM_skip2, MM_rob2 = max(MM_skip2, MM_rob2), MM_skip2 + reward
            
            MM_skip1, MM_rob1 = max(MM_skip1, MM_rob1), MM_skip1 + reward
        
        return max(MM_skip2, MM_rob2, MM_skip1, MM_rob1)