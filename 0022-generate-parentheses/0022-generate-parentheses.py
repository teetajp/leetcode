class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two options:
        # - outside, inside
        
        # OR:
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
        self._helper(0)
        
        
        
        return list(self.combos)
    
    def _helper(self, numOpen):
        numClose = len(self.stack) - numOpen
        
        # base case: can form full string
        if numOpen == numClose == self.n:
            result_str = ''.join(self.stack)
            self.combos.add(result_str)
            return
        
        if numOpen < self.n:
            self.stack.append('(')
            self._helper(numOpen + 1)
            self.stack.pop()
        
        if numOpen > numClose:
            self.stack.append(')')
            self._helper(numOpen)
            self.stack.pop()
        
        
        # removed = stack.pop()
        # no need to update numOpen/numClose as its local to each func call