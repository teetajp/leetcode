class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Define isValid(i, j) as a function that checks whether
        
        11106
        
        at each step, can check 1 or 2 characters (substring)
        - to be valid, substring must be of length 1 or 2
            - if length 1, then must be digits '1' to '9'
            - if length 2, then leading digit must be
                '1' followed by '0' to '9' OR
                '2' followed by '0' to '6'
                
        # inclusive
        Let DP be the number of ways to decode a substring of string s between index i and j (inclusive).
        
        Base Cases:
        
        sslen = j - i + 1
        
        def isValid(i, j):
            if sslen == 1:
                return 1
            elif sslen == 2 and s[i] == '1' and s[j] in {'0' to '9'}:
                return 1
            elif sslen == 2 and s[i] == '2' and s[j] in {'0' to '6'}:
                return 1
            else:
                return 0
        
        Base Case:
        - For all 0 <= i <= n - 1:
            DP[i][i] = isValid(i, i)
        - For all 0 <= i <= n - 2:
            DP[i][i+1] = isValid(i, i+1)
            
        Recursive Case:
        - For j >= i + 2:
            DP[i][j] = DP[i][i] * DP[i+1][j] + DP[i][i+1] * DP[i+2][j]
        
        Fill Order:
            Initialize base cases first
            Iterate over i from n-1 to 0
            
        Final Answer:
            DP[0][n-1]
        """
        
        n = len(s)
        validMessages = { str(i) for i in range(1, 27) }
        def isValid(substr):
            if len(substr) == 1:
                return int(substr in validMessages)
            elif len(substr) == 2:
                return int(substr in validMessages)
            else:
                return 0
        
        DP = [0] * n
        
        DP[n-1] = isValid(s[n-1])
        
        if n < 2:
            return DP[n-1]
        
        DP[n-2] = isValid(s[n-2]) * (DP[n-1] + isValid(s[n-2:]))
        
        for i in reversed(range(n-2)):
            DP[i] = isValid(s[i]) * (DP[i+1] + isValid(s[i:i+2]) * DP[i+2])
        
        print(DP)
        return DP[0]