class Solution(object):
    def shortestSubarray(self, nums, k):

        
        minlen=float('inf')
        deque=[]
        sum=0
        for i,num in enumerate(nums):
            sum=sum+num
            if(len(deque)==0 and nums>=0 ):
             
                deque.append([sum,i])
               
            
            if(len(deque)>0 and sum>deque[-1][0]):
                deque.append([sum,i])
                
                
            else:
                while(len(deque)>0 and sum<=deque[-1][0]):
                 
                    deque.pop()
                    
                  
                deque.append([sum,i])
                    
            if(sum>=k):
                  minlen=min(minlen,i+1)
                 
            while( len(deque)>0 and sum-deque[0][0]>=k) :
                     
                        minlen=min(minlen,deque[-1][1]-deque[0][1]+1)
                        
                        current=deque[0]
                      
                        deque.pop(0)
                        if( len(deque)>0 and sum-current[0]>=k):
                             minlen=min(minlen,(i-current[1]))
                            
                             
        if(minlen==float('inf')):
            return -1
        else:
            return minlen