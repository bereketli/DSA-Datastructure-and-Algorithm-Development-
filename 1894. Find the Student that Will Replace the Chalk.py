class Solution(object):
    def chalkReplacer(self, chalk, k):
        summed = sum(chalk)
        if summed <= k:
            k %= summed
        prefi =0
        for i in range(len(chalk)):
            prefi += chalk[i]
            if prefi > k:
                return i
        """
        chalk = [5,1,5], k = 22
        summed = 11
        summed <= k:
            k %=summed
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        