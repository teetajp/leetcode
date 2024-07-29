class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Strictly increasing subsequence:
        - Define a subsequence of `nums`:
            ss := [nums_i1, nums_i2, ..., nums_ik] where nums[i_j] < nums[i_j+1] < ... < nums[i_k] for 0 <= i_j < ... < i_k < len(nums)
        - Given that len(nums) > 0, there always exists a subsequence of length 1 or more (i.e. a subseq of any elem of nums)
        
        Brute-force:
        - generate all 2^n subsequences of `nums`, then check whether they satisfy the strictly increasing property, and get any subseq that has the maximum length (multiple subsequences may all tie for max length)
        - time: O(2^n)
        - space: O(n)
            
        Dynamic Programming:            
        ```
        Assume n = len(nums) > 0.
        Let maxLIS[i] be the length of the longest strictly increasing subsequence in `nums` from idx 0 to idx i, where nums[i] is included in the sequence.
        
        Base Case:
            maxLIS[0] = 1
        Recursive Case:
            For 0 < i < n,
                maxLIS[i] = 1 + max( 0, max(maxLIS[j] where nums[j] < nums[i] and 0 <= j < i) )
            
        Order of Evaluation:
            Evaluate `maxLIS[i]`
                for i := 0 -> n-1,
                for j < i,
                    j := i-1 -> 0
        
        Final Answer: max(maxLIS)
        
        Time Complexity: O(n^2); We take O(n) to iterate over each element of nums, and for each element, we do a linear scan backwards for j := i-1 -> 0, which takes O(n), so the algorithm takes O(n^2) in total.
        Space Complexity: O(n) for `maxLIS` array
        ```
        
        Further Improvements:
        - use Python's `bisect` module for binary search
            - this will improve time complexity to O(n log(n)) while keeping the space complexity O(n)
        - or use Red-Black tree / Balanced BST, but this will take more time and space, in practice, than binary search alone
        """
        res: int = 1
        n: int = len(nums)
        maxLIS: list[int] = [1] * n # initialize DP array
        
        for i in range(1, n):
            prevMaxLIS = max((maxLIS[j] for j in reversed(range(0, i)) if nums[j] < nums[i]), default=0)
            # length of maxLIS before iteration i, where sequence was lower in value
            
            maxLIS[i] = 1 + prevMaxLIS
            res = maxLIS[i] if maxLIS[i] > res else res
        
        return res