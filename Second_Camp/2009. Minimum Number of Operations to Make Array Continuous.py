class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n

        unique = set(nums)
        newNums = list(unique)
        newNums.sort()

        for i in range(len(newNums)):
            left = newNums[i]
            right = left + n - 1
            j = self.binarySearch(newNums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans

    def binarySearch(self, newNums, target):
        left = 0
        right = len(newNums)

        while left < right:
            mid = (left + right) // 2
            if target < newNums[mid]:
                right = mid
            else:
                left = mid + 1

        return left


        """
        2009. minimum number of operations to make array continuous.
         1) unique
         2) max(nums) - min(nums) == len(nums) - 1
           
           [1, 4, 5, 6, 10, 11, 12]
                        ,8 , 9, 10]5t
        """
        
