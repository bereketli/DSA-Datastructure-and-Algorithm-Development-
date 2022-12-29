class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = float("inf")
        maximum = 0
        for i in range(len(salary)):
            minimum =  min(minimum, salary[i])
            maximum = max(maximum, salary[i])
        return  (sum(salary) - (minimum + maximum)) / (len(salary)  -2)