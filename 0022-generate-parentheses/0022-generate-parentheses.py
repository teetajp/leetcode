from collections import deque

class Parentheses:
    def __init__(self, str, open_count, closed_count):
        self.str = str
        self.open_count = open_count
        self.closed_count = closed_count
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque([])
        queue.append(Parentheses([], 0, 0))
        
        while queue:
            ps = queue.popleft()
            
            if ps.open_count == n and ps.closed_count == n:
                result.append(''.join(ps.str))
            else:
                # open a new parenthesis
                if ps.open_count < n:
                    queue.append(Parentheses(
                        list(ps.str) + ['('],
                        ps.open_count + 1,
                        ps.closed_count))
                
                # close a parenthesis
                if ps.closed_count < ps.open_count:
                    queue.append(Parentheses(
                    list(ps.str) + [')'],
                    ps.open_count,
                    ps.closed_count + 1))
                    
        return result