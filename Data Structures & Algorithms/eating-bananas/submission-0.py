import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_value, max_value = 1, max(piles)
        middle_value = 1
        k = 1

        while min_value <= max_value:
            middle_value = min_value + (max_value - min_value) // 2
            total_time = self.calculateTimeForEating(piles, middle_value)
    
            if total_time > h:
                min_value = middle_value + 1
            else:
                k = middle_value
                max_value = middle_value - 1
        
        return k

    
    def calculateTimeForEating(self, piles: List[int], k: int) -> int:
        h = 0
        for pile in piles:
            h += math.ceil(pile / k)
        return h

