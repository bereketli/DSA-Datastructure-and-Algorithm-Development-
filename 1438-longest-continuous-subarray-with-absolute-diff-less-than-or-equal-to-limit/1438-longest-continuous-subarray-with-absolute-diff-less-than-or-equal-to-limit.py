class Solution(object):
    def longestSubarray(self, nums, limit):
     
        inc_deque=[]
        dec_deque=[]
        maxlen=0
        front_pointer=0
        rear_pointer=0
        inc_deque.append(0)
        dec_deque.append(0)
        while rear_pointer<(len(nums)):
            
            
            
              
               
              
            while len(inc_deque)>0 and nums[inc_deque[-1]]>nums[rear_pointer]:
                     inc_deque.pop()
            if(rear_pointer!=0):
                  inc_deque.append(rear_pointer)
              
            while len(dec_deque)>0 and nums[dec_deque[-1]]<nums[rear_pointer]:
                    dec_deque.pop()
            if(rear_pointer!=0):
                    dec_deque.append(rear_pointer)
            if nums[dec_deque[0]]-nums[inc_deque[0]]<=limit:
               
                       maxlen=max(maxlen,rear_pointer-front_pointer+1)
               
            while nums[dec_deque[0]]-nums[inc_deque[0]]>limit:
                
            
                 if(front_pointer==inc_deque[0]):
                     inc_deque.pop(0)
                 elif(front_pointer==dec_deque[0]):
                     dec_deque.pop(0)
                
                 front_pointer+=1
           
            rear_pointer+=1
           
    
        return maxlen
                
            
        
#         queue=[]
#         maxlen=0
        
               
#                 queue.append(num)
#                 while(max(queue)-min(queue)>limit):
#                     queue.pop(0)
#                 maxlen=max(len(queue),maxlen)
                
#         return maxlen
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        