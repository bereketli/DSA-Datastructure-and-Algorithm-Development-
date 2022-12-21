class Solution(object):
    def productExceptSelf(self, nums):
           output=[]
           prefix=1
           for i in range(len(nums)-1):
                prefix*=nums[i]
                if i==0:
                    output.append(1)
                    output.append(prefix)
                else:
                    output.append(prefix)
           
           prefix=1
           for i in range(len(nums)-1,0,-1):
                    prefix*=nums[i]
             
                    output[i-1]=output[i-1]*prefix
           return output
                    
                
                    
        
      

        