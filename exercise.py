class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        # write your code here
        self.arr = arr
        self.capa =capacity
        self.len = length
        
    def insertEnd(self, value):
        if self.length < self.capacity:
           self.arrd[self.length] = 1
    def removeEnd(self):
        if self.length:
            self.arr[self.length] = 0
   
    def insertMiddle(self, index, value):
        if self.lenght < self.capacity:
           for i in range(index + 1,self.capacity)
    
        self.arr.insert(index, value)
    def removeMiddle(self, index):
        self.arr.pop(index)
    def printArr(self):
        print(self.arr)
    
objectstat = StaticArrays ()
objectstat.insertEnd(7)
objectstat.printArr()
objectstat.removeEnd()
objectstat.printArr()
objectstat.insertMiddle(3, 9)
objectstat.printArr()
objectstat.removeMiddle(3)
objectstat.printArr()