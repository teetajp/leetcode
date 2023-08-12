class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        results.append([]) # empty set
        
        for n in nums:
            # make a copy of all elements in the results list and add current elem to it
            # then append all of this to the results list
            prev_len = len(results)
            for i in range(prev_len):
                results.append(results[i] + [n])
        
        return results