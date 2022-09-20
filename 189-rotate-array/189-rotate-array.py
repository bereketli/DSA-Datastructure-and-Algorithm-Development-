class Solution(object):
    def rotate(self, nums, k):
        nums.reverse()
        k =k % len(nums)
        right=k-1
        left=0
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right-=1
            left +=1
        l = k
        r = len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1
            
        