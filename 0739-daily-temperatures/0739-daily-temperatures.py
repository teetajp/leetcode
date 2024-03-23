class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if we go forward, we have to keep track of the indices to update
        # temp[i-2]=74 temp[i-1] = 75, temp[i] = 73, temp[i+1] = 72, temp[i+2] = 74
        # then, we update indices i and i+1
        # need to keep order consistent

        # keep a stack on indices we have yet to seen warmer temp
        # forward pass
        # when we see a new temp that is higher,
        # > pop and update everything from top of stack till not higher
        answer = []
        stack = [] # keeps track of day indices
        for i in range(len(temperatures)):            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # while exists a previous day cooler than ith day that has not been updated
                prev_idx = stack.pop() # get most recent unupdated cooler day
                answer[prev_idx] = i - prev_idx # num of days between
                
                
            answer.append(0)
            stack.append(i)
        
        
        return answer