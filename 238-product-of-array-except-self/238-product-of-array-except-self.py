class Solution(object):
    def productExceptSelf(self, nums):
           output=[]
           prefix=[nums[0]]*len(nums)
           postfix=[nums[len(nums)-1]]*len(nums)
           for i in range(1,len(nums)):
                  prefix[i]=nums[i]*prefix[i-1]
                  postfix[len(nums)-1-i]=postfix[len(nums)-i]* nums[len(nums)-1-i]
          
        
           for i in range(len(nums)):
                 if i==0:
                    output.append( postfix[1])
                 elif i ==len(nums)-1:
                     output.append(prefix[-2])
                 else:
                     output.append(prefix[i-1]*postfix[i+1])
           
           return output
        
      

        