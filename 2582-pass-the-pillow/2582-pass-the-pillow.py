class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # if 0 then L->R, else L<-R
        roundTime = n - 1 # takes n-1 passes to reach one end from the other
        
        numRounds = time // roundTime # number of end-to-end passes completed
        offset = time % roundTime
        
        if numRounds % 2 == 0: # even number of rounds
            # => current direction is left-to-right
            return offset + 1
        else: # odd number of rounds
            # => current direction is right-to-left
            return n - offset