class Solution(object):
    def longestOnes(self, nums, k):
        count =0
        maxlen =0
        left=0
        for right in range(len(nums)):
            if nums[right] ==0:
                count +=1
            
            while count>k:
                if nums[left] ==0:
                    count -=1
                left +=1
            maxlen = max(maxlen, right - left+1)
          
        return maxlen
        
        