class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        rear = n + m -1
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[rear] = nums1[m - 1]
                m -=1
                rear -=1
            else:
                nums1[rear] = nums2[n - 1]
                n -=1
                rear -=1
        if n > 0:
            nums1[:n] = nums2[:n]
            

     