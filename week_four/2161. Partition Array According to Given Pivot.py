class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        countPivot = 0
        index_gr = {}
        # registering the order of the greater elements
        for i in range(len(nums)):
            if nums[i] == pivot:
                countPivot += 1
            elif nums[i] > pivot:
                index_gr[i] = nums[i]
        # collecting smaller elements to the left
        first = -1
        for i in range(len(nums)):
            if first == -1 and nums[i] >= pivot:
                first = i
                continue
            elif first != -1 and nums[i] < pivot:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
        # inserting elements equal to pivot
        if countPivot:
            for i in range(first,first + countPivot):
                nums[i] = pivot
            first += countPivot
        # enserting elements ordered greater than pivot to nums
        for key in index_gr:
            nums[first] = index_gr[key]
            first += 1
        return nums