class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sln = [[]]
        def power_set(index, arr):
            if index == len(nums):
               return
            for i in range(index , len(nums)):
                new =[nums[i]]
                new = arr + new
                sln.append(new)
                power_set(i + 1, new)
                
            return

        power_set(0,[])
        return sln
