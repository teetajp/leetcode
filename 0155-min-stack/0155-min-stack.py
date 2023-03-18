class MinStack:

    # Since we can only insert and remove at the end,
    # there is a minimum value at each subarray [0 to i] where i < n;
    # and the subarray [0 to i].getMin >= [0 to j].getMin where i < j
    # since the minimum can only get smaller with more elements on added
    def __init__(self):
        self.stack = []
        # the list will consist of tuples (val, min)

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append( (val, min(self.stack[-1][1], val) ) )

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()