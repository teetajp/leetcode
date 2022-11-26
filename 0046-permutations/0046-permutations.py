import math
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # The numbers is nums are distinct, so we don't need to worry about combinations (permutations where that appear the same due to same value showing up more than once).
        # Let n = nums.length; We know that 1 <= n <= 6
        # We can use each number in the nums array once, so that the output is an list with nPr = n! / (n-r)! = n! since r = 3 arrays of size n => O(n*n!) space and time
        
        # Think of it as a n-ary tree with n levels and n! leaf nodes. O(n-r) per node each level to split/copy array
        n = len(nums)
        
        perms = []
        def permuteRecursive(curr: List[int], avail: List[int]):
            if len(avail) == 0:
                nonlocal perms
                perms.append(curr.copy())
            else:
                for i in range(len(avail)):
                    curr.append(avail[i])
                    permuteRecursive(curr, [x for x in avail if x not in curr])
                    curr.pop()
        permuteRecursive([], nums)
        return perms