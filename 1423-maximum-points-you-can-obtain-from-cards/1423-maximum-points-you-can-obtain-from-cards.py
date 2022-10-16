class Solution(object):
    def maxScore(self, cardPoints, k):
        pref =[cardPoints[0]]
        l, minimum=0, float("inf")
        for i in range(1,len(cardPoints)):
            pref.append(pref[i -1] + cardPoints[i])
       
        for i in range(k +1):

            previous = pref[i -1] if i != 0 else 0
           
            minimum =min(minimum , pref[i + len(cardPoints) -1 -k] - previous)
        return pref[-1] - minimum
            
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        