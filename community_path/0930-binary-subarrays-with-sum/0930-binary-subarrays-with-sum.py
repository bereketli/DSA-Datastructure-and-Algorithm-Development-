class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        dic ={0:1}
        count, pref =0, 0
        for i in range(len(nums)):
            pref += nums[i]
            if pref - goal in dic:
                count += dic[pref - goal]
            if pref not in dic:
                dic[pref] = 1
            else:
                dic[pref] +=1
        return count
                
            
        """
         nums = [1,0,1,0,1], goal = 2
         r=4 
         l =1
         sum =2
         count =1
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """