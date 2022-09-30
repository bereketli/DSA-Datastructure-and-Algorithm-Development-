class Solution(object):
    def numberOfSubarrays(self, nums, k):
           ans,right=0,0
           odd_indeces=deque()
           left=-1
            
           
           while right<len(nums):
                if nums[right]%2!=0:
                    odd_indeces.append(right)
                if len(odd_indeces)==k:
                   ans+=odd_indeces[0]-left
                elif len(odd_indeces)>k:
                      left=odd_indeces[0]
                      odd_indeces.popleft()
                      ans+=odd_indeces[0]-left
                right+=1
           return ans
                      
        
 