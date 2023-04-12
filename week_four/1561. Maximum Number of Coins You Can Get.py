class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
       
        sumup =0
        for i in range(len(piles),(len(piles) / 3) -1 ,-2):
            if len(piles) == i:
                continue
            sumup += piles[i]
        return sumup
        """
        :type piles: List[int]
        :rtype: int
        """
        
