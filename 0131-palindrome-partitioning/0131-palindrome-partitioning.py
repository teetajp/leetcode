class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        
        dp = {(i, i): True for i in range(n)}
        palindromes = {(i, i): s[i] for i in range(n)}

        def isPalindrome(start, end):
            # end is inclusive
            if start < 0 or start >= n or end < 0 or end >= n or start > end:
                return False
            elif (start, end) in dp:
                return dp[(start, end)]
            
            if start + 1 == end:
                # adjacent
                dp[(start, end)] = s[start] == s[end]
                if dp[(start, end)]:
                    palindromes[(start, end)] = s[start:end+1]
                
            elif s[start] == s[end] and isPalindrome(start + 1, end - 1):
                dp[(start, end)] = True
                palindromes[(start, end)] = s[start:end+1]
            else:
                dp[(start, end)] = False

            return dp[(start, end)]
                
        
        def DFS(i, completed_parts, new_start):
            if i == n:
                if new_start == i:
                    # previous letter was formed a palindrome partition
                    res.append(completed_parts.copy())
                # otherwise couldn't form partition
                return
            
            # split partition at current index if splittable
            if isPalindrome(new_start, i):
                # cutting the last partition off here forms a palindrome
                completed_parts.append(palindromes[(new_start, i)])
                DFS(i+1, completed_parts, i+1) # next idx is new partition start
                completed_parts.pop()
            
            # no split
            DFS(i+1, completed_parts, new_start)
        
        DFS(0, [], 0)
        
        return res