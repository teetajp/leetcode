class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res, self.stack, self.n = [], [], n
        self._generateParenthesisRecursive(0)
        return self.res
    
    def _generateParenthesisRecursive(self, numOpen):
        # we don't need `numClose` in the param as we can derive it from data
        numClose = len(self.stack) - numOpen
        
        # base case: can form full string
        if numOpen == numClose == self.n:
            self.res.append(''.join(self.stack))
            self.stack.pop()
            return
        
        if numOpen < self.n:
            self.stack.append('(')
            self._generateParenthesisRecursive(numOpen + 1)
        
        if numOpen > numClose:
            self.stack.append(')')
            self._generateParenthesisRecursive(numOpen)
            
        if self.stack:
            self.stack.pop()