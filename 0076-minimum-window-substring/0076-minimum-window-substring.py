class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # iterating through s once
        # keep a counter of character freqs that have been met (freq of 0 or lower)
        # if character not in freqs, then ignore it
        # can use queue or two pointers for the window, use two pointers here to save space
        # => first grow window on right until hit min_freq_met (increment char freqs), then shrink (decrement char freqs) from left to minimize window size
        
        # time: O(m + n) to iterate through s at most twice (once for right pointer and once for left pointer), iterate through t once
        # space: O(n) : Freq dict to keep count of all chars in t. (If we used queue for window, then O(max(m, n)) = O(m + n)
        m, n = len(s), len(t)
        freqs = {}
        
        for char in t:
            freqs[char] = freqs.get(char, 0) + 1
            
        cur_freq_met, min_freq_met = 0, len(freqs)
            
        
        l, r = 0, 0
        min_window_idx = None
        while r < m:
            # expand window to include at least the freq of each char in t
            right_char = s[r]
            
            if right_char in freqs:
                freqs[right_char] -= 1
                
                if freqs[right_char] == 0:
                    cur_freq_met += 1
            
            while cur_freq_met == min_freq_met:
                # shrink window from left to get min window for this instance
                cur_window_len = r - l + 1
                
                if min_window_idx is None or (min_window_idx[1] - min_window_idx[0] + 1 > cur_window_len):
                    if cur_window_len == n: # found best possible window: return early
                        return s[l : r + 1]
                    min_window_idx = (l, r) # update current min window
                
                # shrink left side of window
                left_char = s[l]
                
                if left_char in freqs:
                    # check if shrinking window makes the char freq lower than in t
                    if freqs[left_char] == 0:
                        cur_freq_met -= 1
                        
                    freqs[left_char] += 1
                l += 1 # move left pointer
                    
            r += 1
            
        return s[min_window_idx[0] : min_window_idx[1] + 1] if min_window_idx else ""