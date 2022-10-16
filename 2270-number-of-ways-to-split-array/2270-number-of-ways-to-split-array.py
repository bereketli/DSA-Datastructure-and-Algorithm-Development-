class Solution(object):
    def waysToSplitArray(self, nums):
        post =[0] * len(nums)
        pref,count =0,0
        for i in range(len(nums) - 1, -1, -1):
             if i == len(nums) -1 :
                post[len(nums) -1] = nums[len(nums) -1]
             else:
                post[i] =nums[i] + post[i + 1]
        for i in range(len(nums) - 1):
            pref +=nums[i]
            if pref >= post[i +1]:
                count +=1
        return count
            
            
        
        """
        nums = [10,4,-8,7]
        pref =[10,14,6,13]
        post =[13,3-1,7]
        :type nums: List[int]
        :rtype: int
        """
        