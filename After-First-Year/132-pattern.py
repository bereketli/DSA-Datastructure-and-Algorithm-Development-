class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimum = nums[0]
        stack = []
        for num in nums:
            while stack and stack[-1][1] < num:
                stack.pop()
            if stack and stack[-1][0] < num and stack[-1][1] > num:
                return True
            stack.append([minimum, num])
            minimum = min(minimum, num)
            
        return False
        