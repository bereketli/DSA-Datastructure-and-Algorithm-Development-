class Solution(object):
    def merge(self, intervals):
      
      
        intervals.sort()
      
        output=[]
        interval=0
        while interval<len(intervals):
            current=intervals[interval]
           
            
            for i in range(interval+1,len(intervals)):
                
                if(current[1]>=intervals[i][0] ):
                    if(current[1]<=intervals[i][1] ):
                        current=[current[0],intervals[i][1]]
                    interval=i
                
           
            output.append(current)
            interval+=1
        return output
            
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        