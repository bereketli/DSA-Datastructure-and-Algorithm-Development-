class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mini = [nums[0]]
        maxi = [nums[-1]]
        for num in nums:
            mini.append(min(mini[-1], num))
        for num in nums[::-1]:
            maxi.append(max(maxi[-1], num))
        
        maxi.reverse()

        for i in range(len(nums)):
            if mini[i] < nums[i] < maxi[i]:
                return True
        return False
    



        

