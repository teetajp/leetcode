class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        char_seen = {}
        
        for end, x in enumerate(s):
            # check if we have seen current char 'x'
            while char_seen.get(x, False) == True:
                # move the start ptr and remove chars from list until past the last x
                char_seen[s[start]] = False
                start += 1

            char_seen[x] = True
            maxLength = max(maxLength, end - start + 1)
            
        return maxLength
    # Time Complexity: O(|s|) since iterating over all chars in s
    # Space Complexity: O(1) constant, even though we are storing all unique chars of s in a hash map, the alphabet has a fixed size.
    