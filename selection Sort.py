#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minimum = i-1
        for j in range(i,len(arr)):
            if arr[minimum] > arr[j]:
               minimum = j
        return minimum
        
        # code here 
    
    def selectionSort(self, arr,n):
        self.arr = arr
        for i in range(n):
            
            minimum=self.select(self.arr ,i+1)
           
            
            if minimum != i:
               self.arr[i],  self.arr[minimum] = self.arr[minimum], self.arr[i]
               
            
        return self.arr
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
