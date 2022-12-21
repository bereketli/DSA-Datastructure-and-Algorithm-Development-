class Solution(object):
    def getDescentPeriods(self, prices):
        count, l= 0,0
        for r in range(len(prices)):
            while l< r and prices[r] != prices[r - 1] -1:
                  l +=1
            count += r -l +1
        return count
        """
        :type prices: List[int]
        :rtype: int
        """
        