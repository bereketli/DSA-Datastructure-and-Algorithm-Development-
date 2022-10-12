class Solution(object):
    def minPairSum(self, nums):
        maximum =0
        n = len(nums)
        nums.sort()
        for i in range(len(nums)):
            maximum =max(maximum, nums[i] + nums[n -1 -i])
        return maximum
        """
        :type nums: List[int]
        :rtype: int
        """
        