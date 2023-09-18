class Solution:
    def minSteps(self, n: int) -> int:
        No_A = 1
        operation = 0
        copied = 0
        while No_A < n:
          if n % No_A == 0:
            operation += 1
            copied = No_A

          No_A += copied
          operation += 1
        return operation