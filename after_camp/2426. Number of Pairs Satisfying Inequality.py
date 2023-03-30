class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums1 = [(nums1[i] - nums2[i] )for i in range(len(nums2)) ]
      
        self.count_pair = 0
        def merge(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            
            return merge_sort(left, right)
        def merge_sort(left, right):
            lpt, rpt = 0, 0
            tempo = []
           
            while lpt < len(left) and rpt < len(right):
                if left[lpt] <= right[rpt]:
                    tempo.append(left[lpt])
                    lpt += 1
                else:
                    tempo.append(right[rpt])
                    rpt += 1
            tempo.extend(left[lpt:])
            tempo.extend(right[rpt:])
            
            rpt = 0
            for lpt in range(len(left)):
                while rpt < len(right) and left[lpt] > right[rpt] + diff:
                    rpt += 1
                self.count_pair += len(right) - rpt
           
            return tempo
        merge(nums1)
        return self.count_pair


