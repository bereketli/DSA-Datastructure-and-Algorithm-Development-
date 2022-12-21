class Solution(object):
    def removeElement(self, nums, val):
        l =0
        for r in range( len(nums)):
            if l ==-1 and nums[i] == val:
                 l = r
            else:
                if nums[r] != val:
                   nums[l] , nums[r] = nums[r], nums[l]
                   l +=1
        return l
                    
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        