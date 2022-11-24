class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # store each value in a hashmap and put False as default
        # set to true if we encounter the number
        # if we see it again and the value is in the hashmap (as True), we return False
        # else return True
        # O(n) time complexity since we iterate through the whole array
        # O(1) space since the values are constrained by the range of ints
        #   - maybe O(n) space? not sure, since hash map since grows if there are more distinct vals
        
        values_seen = set()
        
        for val in nums:
            if val in values_seen:
                return True
            values_seen.add(val)
        
        return False