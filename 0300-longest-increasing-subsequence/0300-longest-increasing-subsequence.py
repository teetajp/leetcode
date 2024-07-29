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
        - knapsack? triangular matrix?
        - Candidates:
            - Let maxLIS[i] be the length of the longest strictly increasing subsequence in `nums` from idx 0 to idx i, where nums[i] is included in the subsequence.
                - Need to keep some kind of monotonic stack / queue ? heap?
                - Need to lookback to maxLIS 0 to i-1?
                    - could be O(n^2) runtime, still better than O(2^n) ... could work
                    - look for first value of maxLIS[j] that is than nums[i], use that as baseline?
                        - best would be slightly smaller than nums[i], that would get more length than j that is close to i but has nums[j] a lot less than nums[i] ...
                            - do we still need to look for a smaller one after we find the first one?
                            - could cut search space shorter if we find one a maxLIS[j] close to but less than nums[i], but still need to lookback a bit more, just until length of j is roughly equal to maxLIS[j], since there cant be a subseq longer than length j... but overall still need to check... and doesn't improve runtime by a polynomial factor...
            - Let maxLIS[i] be the length of the longest strictly increasing subsequence in `nums` from idx 0 to idx i.
                - How to keep track of what was the last elem value?
                - maxLIS[i] = max(maxLIS[i-1], max(maxLIS[j] where nums[j] < nums[i]))
                    - compare best maxLIS without including current index nums[i], and the max length subseq including nums[i]
                        - use binary search tree to find next lower index?
                        - binary search to search / insert each elem ---> red-black / AVL tree ---> O( log(n) ) per operation
                            - O(1) to get maxLIS[i-1], O(log n) to find maxLIS[j] where nums[j] < nums[i]
                            - O(n log(n) ) total!!!
                                - use Python's bisect module, or the `sortedcontainers` module
                    - how to find the next lower elem?
                    - reduce from 2D maxLIS[0 <= i <= n-1][True/False] to maxLIS[i] ?
            - monotonic stack/queue approach with no DP?
            
            
        Let's implement the O(n^2) algorithm first, then implement the O(n log n) algorithm later
        
        ```
        Assume len(nums) > 0.
        Let maxLIS[i] be the length of the longest strictly increasing subsequence in `nums` from idx 0 to idx i.
        
        Base Case:
            maxLIS[0] = 1
        Recursive Case:
            For 0 < i < n,
                maxLIS[i] = max( maxLIS[i-1], 1 + max(maxLIS[j] where nums[j] < nums[i] and 0 <= j < i) )
            
        Order of Evaluation:
            Evaluate `maxLIS[i]`
                for i := 0 -> n-1,
                for j < i,
                    j := i-1 -> 0
        
        Final Answer: maxLIS[n-1]
        
        Time Complexity: O(n^2); We take O(n) to iterate over each element of nums, and for each element, we do a linear scan backwards for j := i-1 -> 0, which takes O(n), so the algorithm takes O(n^2) in total.
        Space Complexity: O(n) for `maxLIS` array
        ```
        """
        n: int = len(nums)
        maxLIS: list[int] = [1] * n # initialize DP array; lower bound of all answer is 1 (subseq with just the element)
        res = 1
        for i in range(1, n):
            
            # length of maxLIS before iteration i, where sequence was lower in value
            maxLIS[i] = 1 + max((maxLIS[j] for j in reversed(range(0, i)) if nums[j] < nums[i]), default=0)
            res = max(res, maxLIS[i])
        
        
        return res
        