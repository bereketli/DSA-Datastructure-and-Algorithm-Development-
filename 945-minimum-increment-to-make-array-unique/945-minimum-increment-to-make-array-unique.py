class Solution(object):
    def minIncrementForUnique(self, nums):
          counted = Counter(nums)
          step =0
          repetion =[]
          for num in range(len(nums) +max(nums)):
                if counted[num] >1:
                    repetion = repetion + ( [num] * (counted[num] -1))
                elif repetion and num not in counted:
                    step += num - repetion.pop()
          return step
       