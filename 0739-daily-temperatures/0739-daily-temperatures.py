class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # keeps track of day indices that have not seen warmer day
        for i in range(len(temperatures)):            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # while exists a previous day cooler than ith day that has not been updated
                prev_idx = stack.pop() # get most recent unupdated cooler day
                answer[prev_idx] = i - prev_idx # num of days between
                          
            #answer.append(0)
            stack.append(i)
        
        return answer
    # time: O(n) for accessing each element at most twice
    # space: O(n) for stack and answer list