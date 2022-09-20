class Solution(object):
    def rotate(self, nums, k):
        store=[]
        if k==len(nums):
            return
            
        if len(nums)<k:
            k=k %len(nums)
        for i in range(k):
               store.append(nums.pop())
        store.reverse()
        play=store+nums
       
        for i in range(len(play)):
              if i <len(nums):
                  nums[i]=play[i]
              else:
                nums.append(play[i])
            
            
            
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        