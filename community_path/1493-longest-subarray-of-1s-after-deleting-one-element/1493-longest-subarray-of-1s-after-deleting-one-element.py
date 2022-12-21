class Solution(object):
    def longestSubarray(self, nums):
        l,r,count0 =0,0,0
        subarray =0
        while r < len(nums):
            if nums[r] ==0:
                count0 +=1
            while count0 > 1:
                if nums[l]  == 0:
                    count0 -=1
                l +=1
            subarray = max(subarray, r -l)
            r +=1
        return subarray
        """
        nums = [0,1,1,1,0,1,1,0,1]
        count =2
        l=5
        r=7
        subarr= 5
        :type nums: List[int]
        :rtype: int
        """
        