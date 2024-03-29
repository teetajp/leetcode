class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # rate limited by the car at the top
        
        # number of unique car speeds and position at the end
        # all positions unique, so no need for secondary key
        pos_speed = sorted(zip(position, speed), key = lambda x : x[0])
        num_fleets = n # there is always at least one car
        
        print(pos_speed)
        
        pos_ahead, speed_ahead = pos_speed.pop() # car closest to dest
        tta_ahead = (target - pos_ahead) / speed_ahead
        
        while pos_speed:
            pos_cur, speed_cur = pos_speed.pop()
            
            tta_cur = (target - pos_cur) / speed_cur
            
            # to "catch up", tta of cur car must be <= tta of car ahead;
            # increment car fleet when cur car cant catch up with the one ahead
            if tta_cur > tta_ahead:
                tta_ahead = tta_cur
            elif tta_cur <= tta_ahead:
                # set cur car as "ahead" for next iteration
                # tta of cur car is bounded by tta of the car ahead
                num_fleets -= 1
                
            pos_ahead, speed_ahead = pos_cur, speed_cur
        
        
        return num_fleets