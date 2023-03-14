class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] >= arr[mid + 1]:
                r = mid -1
            else:
                l = mid + 1
        return l


        """
        find i
        using binary search
        l <- 0, r <- the last index
        findd mid = (l + r) // 2
        if value mid  >= value mid + 1,mid vlaue is either i or in the right of i
        if value mid index < value of mid + 1 , mid vlaue is in the left of i
        """

        
        