class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        minimum = 0
        maximum = 0
        pref = 0
        for diff in differences:
            pref += diff
            minimum = min(minimum, pref)
            maximum = max(maximum, pref)
        result = (upper - maximum) - (lower - minimum) + 1
        return  result if result > 0 else 0
        """
        differences = [1, -3, 4]
        prefix =[1,-2,2]
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        