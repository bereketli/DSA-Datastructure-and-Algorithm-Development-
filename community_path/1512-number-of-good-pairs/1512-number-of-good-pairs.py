class Solution(object):
    def numIdenticalPairs(self, nums):
        count =0
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                   count +=1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        