class Solution:
    def jump(self, nums: List[int]) -> int:
        # We need a way to keep track of number of jumps
        # We could keep an array of min jumps to reach each index i
        # Particularly, wea re interested in the min umps to reach indexes that can reach nums[n-1]
        # We want the minimal size subsequence with start position nums[0] whose sum reaches each index in the subsequence and the total sum = n - 1
        # We could update the array in each iteration
        
        # Let minJumps(i) be the minimum number of jumps(elements visited) needed to get from nums[0] to index i such that the sum of the subsequence adds up to i.
        # shortest subsequence whose sum adds up to i.
        n = len(nums)
        minJumps = [inf] * n
        minJumps[0] = 0
        # O(n*(n+1) / 2) = O(n^2) if we iterate through nums and update minJumps at each step
        for i in range(n):
            min_to_i = minJumps[i]
            if min_to_i != inf:
                for j in range(i, min(n, i + nums[i] + 1)):
                    minJumps[j] = min(minJumps[j], min_to_i + 1)
        return minJumps[n-1]
        
        