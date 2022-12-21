class Solution(object):
    def longestWPI(self, hours):
        dic={0:-1}
        maxlen,prefi =0, 0
        for i in range(len(hours)):
            app = 1  if hours[i] >  8 else -1
            prefi +=app
            if prefi not in dic:
                dic[prefi] = i
            if prefi -1 in dic:
                maxlen = max(maxlen, i - dic[prefi -1])
            if prefi>0:
                maxlen = max(maxlen, i +1)
                
        return maxlen
            
        
        """
        :type hours: List[int]
        :rtype: int
        """
        