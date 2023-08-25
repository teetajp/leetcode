class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        # use stack to keep track of days that still need warmer temp
        # the stack will only increase in size as long as the item on top is less than the item below it (otherwise it would be popped as the top element, which is the newest day, would be warmer than the previous in that case)
        stack = [(0, temperatures[0])]
        
        for i in range(1, n):
            while stack and temperatures[i] > stack[-1][1]:
                answer[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
                
            stack.append((i, temperatures[i]))
            
        return answer
    # Time Complexity: O(n) -> for loop iterates over n elems, inner loop max n
    # Space Complexity: O(n) -> for stack and answer