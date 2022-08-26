class Solution(object):
    def rearrangeArray(self, nums):
        for i in range(1,len(nums)-1):
            if i<=len(nums)-2 and (nums[i-1]<nums[i] and nums[i]<nums[i+1]) or (nums[i+1]<nums[i] and nums[i]<nums[i-1]):
                      store=nums[i+1]
                      nums[i+1]=nums[i]
                      nums[i]=store
                        
                
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        