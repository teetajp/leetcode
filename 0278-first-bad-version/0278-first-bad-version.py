# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # We want to find the pair where the first val is False and second is True and return second
    def firstBadVersion(self, n: int) -> int:
        def binarySearch(l: int, r: int) -> int:
            if isBadVersion(l): return l
            lm, rm = l + (r - l) // 2, l + (r - l) // 2 + 1
            lmbad, rmbad = isBadVersion(lm), isBadVersion(rm)
            if lmbad: # lm is bad, so not first, so check lower
                return binarySearch(l + 1, lm)    
            elif rmbad: # left is False, right is True, so first is right
                return rm
            else: # rm is not bad, so check higher
                return binarySearch(rm + 1, r)
            
        return binarySearch(1, n)