class Solution(object):
    def removeDuplicates(self, nums):
        l =0
        for r in range(1,len(nums)):
            if nums[r] > nums[l]:
                l +=1
                nums[l] = nums[r]
        return l + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        