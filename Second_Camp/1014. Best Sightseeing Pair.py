class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res, mx_val = 0, values[0] - 1
        for i in range(1, len(values)):
            res = max(res, mx_val + values[i])
            mx_val = max(mx_val, values[i]) - 1
        return res


        
