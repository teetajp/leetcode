class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0
        
        for n in nums:
            # check only start of sequences (numbers that have no left neighbor in the set)
            if n - 1 not in numsSet:
                length = 0
                while n + length in numsSet:
                    length += 1
                maxLength = max(maxLength, length)
                
        return maxLength