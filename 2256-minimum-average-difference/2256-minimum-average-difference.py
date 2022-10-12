class Solution(object):
    def minimumAverageDifference(self, nums):
        summed =sum(nums)
        min_diff =[float("inf"),0]
        pref =0
        for i in range(len(nums)):
        
            pref += nums[i]
            if i <len(nums) -1:
                diff = abs((pref / (i + 1) ) - ((summed -pref) / (len(nums) -i -1)))
            else:
                diff =abs(pref / (i + 1) )
            if diff < min_diff[0]:
                min_diff=[diff, i]
            
            
        return min_diff[1]
        """
        nums = [2,5,3,9,5,3]
        
        :type nums: List[int], 
        :rtype: int
        """
        