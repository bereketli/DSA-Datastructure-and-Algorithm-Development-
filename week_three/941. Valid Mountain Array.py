class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index = 0
        flag = False
        while index < len(arr) -1 and arr[index] < arr[index + 1]:
             index += 1
       
        while index and index < len(arr) -1 and arr[index] > arr[index + 1]:
             flag = True
             index += 1
        return False if index != len(arr) -1 or len(arr) < 3 or not flag else True

            
        

