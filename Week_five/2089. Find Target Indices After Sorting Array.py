class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(nums)):
            current=nums[i]
            j=i-1
            while j>=0 and nums[j]>current:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=current
        for i in range(len(nums)):
            if target==nums[i]:
                output.append(i)
            
        return output