class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Start at house 1 or 2 (may need two passes).
        
        We use 0-based indexing to implement, so house 1 is index 0.
        
        Let n be the number of houses along the street minus 1.
        Let MM[i, j] be the maximum amount of money earnable starting from the i-th house up until the n-th house/end of the street if we rob (j=1) / skip (j=0) this house.
        
        Final answer: max(MM[0, 0], MM[0, 1])
        
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
            
        # Time: O(n)
        # Space: O(n)
        
        Optimization:
        - reuse `nums` instead of adding it again
        - pop rewards from `nums` to shrink space instead of just calling it
        
        Optimized Time: O(n)
        Optimized Space: O(1)
        """
        
        MM_skip, MM_rob = 0, nums.pop()
            
        while nums:
            MM_skip, MM_rob = max(MM_skip, MM_rob), nums.pop() + MM_skip

        return max(MM_skip, MM_rob)