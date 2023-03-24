class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.countpair = 0

        #merge and sort divided elements
        def merge(arr1, arr2):
            pt1 = 0
            pt2 = 0
            merged = []
            while pt1 < len(arr1) and pt2 < len(arr2):
                if arr1[pt1] <= arr2[pt2]:
                    merged.append(arr1[pt1])
                    pt1 += 1
                else:
                    merged.append(arr2[pt2])
                    pt2 += 1
            merged.extend(arr1[pt1:])
            merged.extend(arr2[pt2:])

            #find how much numbers satisifies nums[i] > 2 * nums[j]
            #using binary search
            for num in arr2:
                index = bisect.bisect_right(arr1, 2 * num)
                if len(arr1) - index >= 1:
                    self.countpair += len(arr1) - index
            return merged

         #divide elments into half
        def mergeSort(arr):
            l = 0
            r = len(arr) - 1
            if len(arr) <= 1:
                return arr
            mid = (l + r) // 2
            left = mergeSort(arr[l: mid + 1])
            right = mergeSort(arr[mid + 1: r + 1] )
            return merge(left, right)
        mergeSort(nums)
        return self.countpair


