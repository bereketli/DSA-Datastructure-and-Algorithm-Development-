class Solution(object):
    def numberOfSubarrays(self, nums, k):
        dictionary ={0:1}
        pref_sum =0
        count =0
        for i,value in enumerate(nums):
                nums[i] %=2
        
        for num in nums:
            
            pref_sum +=num
            if pref_sum-k in dictionary:
                count += dictionary[pref_sum - k]
            if pref_sum in dictionary:
                dictionary[pref_sum] +=1
            else:
                dictionary[pref_sum] =1
        
        return count
                
                      
        
 