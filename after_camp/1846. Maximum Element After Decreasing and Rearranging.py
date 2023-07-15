class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        arr[0] = 1
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            if diff > 1:
                arr[i] = arr[i] - diff + 1
        return arr[n-1]
