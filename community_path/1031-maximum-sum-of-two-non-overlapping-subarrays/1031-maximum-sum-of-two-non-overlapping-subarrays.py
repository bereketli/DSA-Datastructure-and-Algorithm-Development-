class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        for i in range(1,len(nums)):
                nums[i] += nums[i-1]
        totalsum,firstsum,secondsum = 0,0,0
       
        for right in range(len(nums)-firstLen+1):
            if right == 0:
                firstsum = nums[right + firstLen-1]
            else:
                firstsum = nums[right + firstLen - 1] - nums[right-1]
            second_right=right+firstLen+secondLen-1
          
            while second_right < len(nums):
               
                secondsum = max(secondsum,nums[second_right] - nums[ second_right - secondLen ])
                second_right +=1
            second_left =right-secondLen
            
            while second_left>0:
                               
                                
                                secondsum=max(secondsum, nums[second_left + secondLen -1]-nums[second_left-1])
                               
                                second_left -=1
            if second_left == 0:
                              
                                secondsum=max(secondsum, nums[second_left +secondLen -1])
                                
            totalsum = max(totalsum, firstsum + secondsum)
            
            firstsum,secondsum=0,0
        return totalsum
            
            
                
            
            
            
            
            
            
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        