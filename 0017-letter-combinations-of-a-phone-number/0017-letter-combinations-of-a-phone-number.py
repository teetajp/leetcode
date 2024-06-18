class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ltr_map = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        res = [[]]
        for i in digits:
            init_len = len(res)
            # make extra copies
            for j in range(len(ltr_map[i]) - 1):
                for k in range(init_len):
                    res.append(res[k].copy())
                    
            for j in range(len(ltr_map[i])):      
                # add letter to the combos
                for k in range(init_len):
                    res[j*init_len + k].append(ltr_map[i][j])
            
            
        
        
        return ["".join(ltr_combo) for ltr_combo in res] if len(digits) > 0 else []