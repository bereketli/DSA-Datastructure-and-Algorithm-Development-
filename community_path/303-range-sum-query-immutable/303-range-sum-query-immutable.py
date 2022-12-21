class NumArray(object):

    def __init__(self, nums):
         
         self.nums=nums
     
        

    def sumRange(self, left, right):
      
        
        return sum(self.nums[:right+1])-sum(self.nums[:left])
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)