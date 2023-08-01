class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # check if any substring of s2 has the same frequency as all the chars in s1
        # we need a sliding window of size len(s1)
        
        # as we create the window, increment the count of each char in the window/substring
        # keep a count of the number of chars that has matching count and increment it when we expand the window that match
        # decrement the match count when we shrink the window and the number of chars in the window doesn't match s1
        
        s1_counter = defaultdict(int)
        for letter in s1:
            s1_counter[letter] += 1
        
        s2_counter = defaultdict(int)
        match_needed = len(s1_counter)
        matched = 0
        
        start_idx = 0
        for end_idx, end_letter in enumerate(s2):
            s2_counter[end_letter] += 1
            if s2_counter[end_letter] == s1_counter[end_letter]:
                matched += 1

            if end_idx >= len(s1):
                # increment start_idx and shrink sliding window to make it the right size
                start_letter = s2[start_idx]
                s2_counter[start_letter] -= 1
                
                if s2_counter[start_letter] == s1_counter[start_letter] - 1:
                    matched -= 1

                start_idx += 1
            
            if matched == match_needed:
                return True
        
        return False
    
    # Time complexity: O(n) since we scan s1 and s2 once
    # Space complexity: O(1) since we used a dictionary that stores a maximum of 26 characters
                
        