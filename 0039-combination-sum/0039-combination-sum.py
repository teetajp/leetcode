class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort in decreasing order
        # so we can try to sum larger nums first then fit smaller
        # and skip summing candidates that are too big to save time
        candidates.sort(reverse=True)
        res = []
        
        def combinationSumRec(combo: List[int], cand_idx: int, target: int):
            
            if target > 0 and cand_idx < len(candidates):
                # can still add more numbers
                
                # option 1: try same candidate if not too big
                if candidates[cand_idx] <= target:
                    combo.append(candidates[cand_idx])
                    combinationSumRec(combo, cand_idx, target - candidates[cand_idx])
                    del combo[-1]
                
                # option 2: try another candidate
                combinationSumRec(combo, cand_idx + 1, target)
                
            elif target == 0:
                # our combo sums up to target
                res.append(combo.copy())         
                
        combinationSumRec([], 0, target)
                
        return res
    
# Time Complexity: O(n log n + 2^(target / min(candidates)) or O(nlogn + 2^target)
# Space Complexity: O(n + target)