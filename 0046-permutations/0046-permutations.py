import math
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Let n = nums.length; We know that 1 <= n <= 6
        
        # Think of it as a n-ary tree with n levels and n! leaf nodes. O(n-r) per node each level to copy the remaining int and pass them to recursive function.
        n = len(nums)
        
        perms = []
        def permuteRecursive(curr: List[int], avail: List[int]):
            # Check if we have reached base case when no integers left to select
            if len(avail) == 0:
                # Use this to reference perms, which is outside the recursive function
                nonlocal perms 
                # Need to deep copy otherwise Python will simply copy the reference to curr, the function arg, which will get deallocated after the function returns and we pop elements out of curr.
                perms.append(curr.copy()) 
            else:
                for i in range(len(avail)):
                    curr.append(avail[i])
                    permuteRecursive(curr, [x for x in avail if x not in curr])
                    curr.pop()
        permuteRecursive([], nums)
        return perms
    # O(n*n!) time and space