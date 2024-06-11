class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we need to establish a strict order so that
        # we do not get accidental duplicates in the subset
        # ** this is not permutation but a subset
        
        freq = Counter(nums)
        res = [[]]
        # for each distinct number, need to include all the prev arrays without that number, and all the prev arrays with that number
        # for a duplicate number, just need to copy only the LAST made array and add to it
        
        for num in freq:
            prev_len = len(res) # len before adding this distinct num
            # copy the prev arrays
            res.extend(res[i].copy() + [num] for i in range(len(res)))
            # we have added this num to all the powerset once
            # now need to add duplicates by copying the newly created arrays and appending to them
            
            freq[num] -= 1
            while freq[num] > 0:
                cur_len = len(res)
                for i in range(prev_len, len(res)):
                    res.append(res[i].copy() + [num])
                freq[num] -= 1
                prev_len = cur_len
                
        return res