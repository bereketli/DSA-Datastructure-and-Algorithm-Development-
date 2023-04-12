class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimum = float(inf)
        stack = []
        for num in nums:
            while stack and stack[-1][1] < num:
                stack.pop()
            if stack and stack[-1][0] < num and stack[-1][1] > num:
                return True
            minimum = min(minimum, num)
            stack.append([minimum, num])
        return False
