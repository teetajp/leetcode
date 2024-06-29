class Solution:
    def numDecodings(self, s: str) -> int:
        """
        at each step, can check 1 or 2 characters (substring)
        - to be valid, substring must be of length 1 or 2
            - if length 1, then must be digits '1' to '9'
            - if length 2, then leading digit must be
                '1' followed by '0' to '9' OR
                '2' followed by '0' to '6'
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
        
        DP[n-2] = isValid(s[n-2]) * DP[n-1] + isValid(s[n-2:])
        
        for i in reversed(range(n-2)):
            DP[i] = isValid(s[i]) * DP[i+1] + isValid(s[i:i+2]) * DP[i+2]
        
        return DP[0]