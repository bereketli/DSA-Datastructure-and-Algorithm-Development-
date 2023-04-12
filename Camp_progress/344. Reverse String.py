class Solution:
    def reverseString(self, s: List[str]) -> None:
       def reverse(arr):
            if len(arr) == 1:
                print("base", arr)
                return arr
            mid = len(arr) // 2
            left = reverse(arr[0: mid])
            right = reverse(arr[mid:])
            print("right", right)
            if not right:
                right = []
            if not left:
                left = []
            
            return left.extend(right)
       return reverse(s)
         
