class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        left = 1
        res = 0

        while left <= r:
            bananas = (r + left) // 2

            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p / bananas)
            
            if totalHours <= h:
                res = bananas
                r = bananas - 1
            else:
                left = bananas + 1
        
        return res
        
