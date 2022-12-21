class Solution(object):
    def waysToSplitArray(self, nums):
        summed =sum(nums)
        pref,count =0,0
        for i in range(len(nums) - 1):
            pref +=nums[i]
            if pref >= summed - pref:
                count +=1
        return count
            
            
        
        """
        nums = [10,4,-8,7]
        pref =[10,14,6,13]
        post =[13,3-1,7]
        :type nums: List[int]
        :rtype: int
        """
        