class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # similar to edit distance
        freq = {}
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            cur_letter = s[r]
            freq[cur_letter] = freq.get(cur_letter, 0) + 1
            
                
            # contract the string until its valid
            while (r - l + 1) - max(freq.values()) > k: # when we need more replacement than we have
                letterToRemove = s[l]
                freq[letterToRemove] -= 1
                l += 1
                # may need to update best letter here?
            
            max_length = max(r - l + 1, max_length) 
            r += 1
        
        return max_length
            