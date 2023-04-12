class Solution(object):
    def largestNumber(self, nums):
        def comparator(numPrev,num):
              len_prev=len(str(numPrev))
              len_num=len(str(num))
              concat1=numPrev*(10**len_num)+num
              concat2=num*(10**len_prev)+numPrev
              if concat1>=concat2:
                          return True
              else:
                          return False
        for i in range(len(nums)):
            j=i-1
            current=nums[i]
            while j>=0 and not comparator(nums[j],current):
                    nums[j+1]=nums[j]
                    j-=1
            nums[j+1]=current
        if nums[0]==0:
            return '0'
        output="".join(str(num) for num in nums)
        return output
                  
        """
        :type nums: List[int]
        :rtype: str
        """
        
