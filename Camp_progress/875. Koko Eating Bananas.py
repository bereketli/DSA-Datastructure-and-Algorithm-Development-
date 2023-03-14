class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            rate = (l + r) // 2
            hours_in_rate = 0
            for pile in piles:
                hours_in_rate += ceil(pile/ rate)
            if hours_in_rate <= h:
                r = rate - 1
            else:
                l = rate + 1
        return l
   
        