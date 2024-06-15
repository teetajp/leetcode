class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        
        res = []
        
        def comboSumRec(combo: List[int], cand_idx: int, target: int):
            if target == 0:
                res.append(combo.copy())
                
            elif target > 0 and cand_idx < len(candidates):
                # option 1: include this num
                if candidates[cand_idx] <= target:
                    combo.append(candidates[cand_idx])
                    comboSumRec(combo, cand_idx + 1, target - candidates[cand_idx])
                    combo.pop()
                    
                # option 2: if skip this num, then skip all instances of this num
                while ( cand_idx + 1 < len(candidates) and
                        candidates[cand_idx] == candidates[cand_idx + 1] ):
                    cand_idx += 1 # increment until we see another unique candidate
                
                if cand_idx + 1 < len(candidates):
                    # only if there was another distinct candidate after cur candidate
                    comboSumRec(combo, cand_idx + 1, target)
        
        
        comboSumRec([], 0, target)
        return res
    
# Time complexity: O(nlogn + 2^n)
# Space complexity: O(2^n)