class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Once a group makes a straight, then discard that group.
        
        Draw card until hand is empty:
        - if new card is same as prev card (last card in last group on stack), create a new group
        - if new card is consecutive to prev card (value is +1 of prev card), append to group on top of stack
            - if group on top of stack is full, discard
        - else (if card val is not equal to or 1 greater than prev card, return False)
        
        return true if all groups were discarded and hand is empty
        """
        if len(hand) % groupSize != 0:
            return False # cannot cleanly divide hand by groupSize
        elif groupSize == 1:
            return True
        
        hand.sort() # sort so that duplicates are next to each other
        groups = deque()
        prevCard = hand[-1]
        
        while hand:
            card = hand.pop()
                
            # try to find a spot for the card
            for grp in groups:
                if grp[-1] == card + 1:
                    grp.append(card)
                    
                    if len(grp) == groupSize:
                        groups.remove(grp)
                    break
            else:
                groups.append([card])
                
            prevCard = card
            
        return len(groups) == 0