class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Two options:
        # open, close

        # at the end:
        # - numOpen == numClose = n
        
        # at any point:
        # - numOpen >= numClose (cannot have more close than open)
        
        # when numOpen >= numClose:
        # - can either open more if numOpen < n (otherwise 1 option)
        # - or close
        
        # when we open one, can open more or close
        # - can only open more when numOpen < n
        self.combos = set()
        self.stack = []
        self.n = n
        self._generateParenthesisRecursive(0)
        
        return list(self.combos)
    
    def _generateParenthesisRecursive(self, numOpen):
        # we don't need `numClose` in the param as we can derive it from data
        numClose = len(self.stack) - numOpen
        
        # base case: can form full string
        if numOpen == numClose == self.n:
            result_str = ''.join(self.stack)
            if result_str not in self.combos:
                self.combos.add(result_str)
            return
        
        if numOpen < self.n:
            self.stack.append('(')
            self._generateParenthesisRecursive(numOpen + 1)
            self.stack.pop()
        
        if numOpen > numClose:
            self.stack.append(')')
            self._generateParenthesisRecursive(numOpen)
            self.stack.pop()