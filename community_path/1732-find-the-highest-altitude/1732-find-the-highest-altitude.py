class Solution(object):
    def largestAltitude(self, gain):
        max_sum,prefix_sum =0,0
        for point in gain:
            prefix_sum += point
            max_sum = max(max_sum, prefix_sum)
        return max_sum
        """
        :type gain: List[int]
        :rtype: int
        """
        