# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        peak = self.findPeakElement(mountainArr)
        first_try = self.binarySearch(mountainArr, target, 0, peak)
        if first_try == -1:
            return self.binarySearch(mountainArr, target, peak + 1, mountainArr.length() - 1)
        return first_try

    def findPeakElement(self, nums):
        start = 0
        end = nums.length() - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums.get(mid) > nums.get(mid + 1):
                end = mid
            else:
                start = mid + 1
        return start

    def binarySearch(self, arr, target, start, end):
        isAsc = arr.get(start) < arr.get(end)

        while start <= end:
            mid = start + (end - start) // 2

            if arr.get(mid) == target:
                return mid

            if isAsc:
                if arr.get(mid) < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if arr.get(mid) > target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

        
