class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # no duplicate subsets possible as long as there are one of
        # each unique element in the array and we change each iteration
        res = [[]] # start with set containing empty set
        
        for int_elem in nums:
            for i in range(len(res)):
                res.append(res[i].copy() + [int_elem])
        
        return res