class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        numOdd = 3
        while arr and numOdd > 0:
            i = arr.pop()
            
            if i % 2 == 1:
                numOdd -= 1
            else:
                numOdd = 3
            
        return numOdd == 0