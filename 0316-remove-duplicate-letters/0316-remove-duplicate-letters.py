class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = { char: i for i, char in enumerate(s) }
        occurred = set()
        res = []
        
        for i, char in enumerate(s):
            
            if char not in occurred:
                while res and char < res[-1] and i < lastIndex[res[-1]]:
                    # if current letter is lexicographically smaller than the prev letter
                    # and the prev letter can be inserted later in the string
                    prevChar = res.pop()
                    occurred.remove(prevChar)
                
                occurred.add(char)
                res.append(char)
                    
            
        return "".join(res)