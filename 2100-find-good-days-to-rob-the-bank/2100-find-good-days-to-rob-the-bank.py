class Solution(object):
    def goodDaysToRobBank(self, security, time):
        previous =[0] * len(security)
        next =[0] * len(security)
        prefi1, prefi2 =0, 0
        n = len(security)
        output =[]
         
        for i in range(1,len(security)):
            if security[i] <= security[i - 1] :
                prefi1 +=1
            else:
                prefi1 =0
            if security[n -1 -i] <= security[n -i]:
                prefi2 +=1
            else:
                prefi2 =0
            previous[i] = prefi1
            next[n - 1 -i] = prefi2
        for i,value in enumerate(previous):
            if previous[i] >=time and next[i] >= time:
                output.append(i)
        return output
    
            
            
        
            
                
     
                             
            
            
        
            
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        