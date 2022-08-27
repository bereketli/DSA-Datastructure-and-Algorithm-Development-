class Solution(object):
    def kthLargestNumber(self, nums, k):
        store=[eval(num) for num in nums]
        store.sort()
        return str(store[len(store)-k])
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        