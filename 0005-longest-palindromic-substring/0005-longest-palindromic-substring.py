class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Beginning from shortest to longest length,
        only indices of shorter length that are palindromic may be palindromic at longer lengths, given that each character pair surrounding them are also the same.
        
        Let isPLD(i, j) output whether the substring starting at index i ending at index j (exclusive) is a palindrome.
        
        Iterate k from 1 to len(s):
            Iterate i from 0 to len(s) - k:
            return the first s[i:i+k] such that isPLD(i, i+k)
            
        Base Cases:
        - if i == j:
            isPLD(i, j) := True
        - if 0 <= i < len(s) and j == i + 1
            isPLD(i, j) := True
        - if j <= i, isPLD(i, j) := False

        Recursive Case:
        - Assume i < j, let sslen := len(s[i:j])
        - # odd and even cases are handled by base case
            isPLD(i, j) := isPLD(i + 1, j - 1) and s[i] == s[j-1]
            
        Bottom up DP
        """
        n = len(s)
        
        if n == 0:
            return ""
        if n <= 2:
            return s if s[0] == s[-1] else s[0]
        
        isPLD = [[False] * (n+1) for _ in range(n)]
        
        # base cases
        for i in range(n):
            isPLD[i][i] = True # empty string is always a palindrome
            
            if i+1 < n:
                isPLD[i][i+1] = True # string of len 1 is always a palindrome
        
        # recursive case
        res = [0, 1]
        
        for k in range(2, n+1): # check every substring starting from len 2
            for i in range(0, n - k + 1): # start index of substring
                j = i + k # end index (exclusive)
                
                if isPLD[i][j]:
                    continue
                    
                isPLD[i][j] = isPLD[i+1][j-1] and (s[i] == s[j-1])
                
                if isPLD[i][j] and j - i >= res[1] - res[0]:
                    res[0], res[1] = i, j
            
        return s[res[0]:res[1]]
        