class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort() # sort to ensure candidates are ordered
        
        # try in decreasing or increasing order of candidate magnitude
        res = []
        
        def combinationSumRec(combo: List[int], cand_idx: int, target: int):
            
            if target > 0 and cand_idx < len(candidates):
                # can still add more numbers
                
                # option 1: try same candidate
                combo.append(candidates[cand_idx])
                combinationSumRec(combo, cand_idx, target - candidates[cand_idx])
                del combo[-1]
                
                combinationSumRec(combo, cand_idx + 1, target)
                
            elif target == 0:
                # our combo sums up to target
                res.append(combo.copy())         
                
        combinationSumRec([], 0, target)
                
        return res