class Solution(object):
    def findDuplicate(self, nums):
        diction = {}
        for i in range(len(nums)):
            if nums[i] not in diction:
                diction[nums[i]] = 1
            else:
                return nums[i]
        
        """

        
        :type nums: List[int]
        :rtype: int
        """
        