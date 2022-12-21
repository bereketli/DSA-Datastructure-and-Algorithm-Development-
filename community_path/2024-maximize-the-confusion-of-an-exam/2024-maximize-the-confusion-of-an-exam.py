class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        t,f,l =0,0,0
        max_con =0
        for r in range(len(answerKey)):
            if answerKey[r] =="T":
                t +=1
            else:
                f +=1
            while min(t,f) > k:
                
                if answerKey[l] == "T":
                    t -=1
                else:
                    f -=1
                l +=1
            max_con = max(max_con, t + f) 
        return max_con
            
        
        
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        