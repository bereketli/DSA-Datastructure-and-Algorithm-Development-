class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums) -1, 0, -1):
            if nums[i] > nums[i -1]:
                        minimum =i 
                        for k in range(i +1, len(nums)):
                            if nums[i -1] < nums[k] and nums[minimum] >= nums[k]:
                                minimum =k
                           
                        
                        nums[i - 1], nums[minimum] = nums[minimum], nums[i - 1]
                        rev = len(nums) -1
                        while i < rev:
                            nums[i] , nums[rev] = nums[rev], nums[i]
                            i +=1
                            rev -=1
                        return nums
        return nums.sort()
            
            
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        