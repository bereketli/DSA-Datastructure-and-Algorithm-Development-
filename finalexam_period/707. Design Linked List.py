class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.dummy = Node(None)
    
    def get(self, index: int) -> int:
        i = -1
        tempo = self.dummy
        while tempo.next is not None:
           
            if i == index - 1:
                return tempo.next.value
            tempo = tempo.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        tempo = self.dummy.next
        self.dummy.next = newNode
        newNode.next = tempo

    def addAtTail(self, val: int) -> None:
        tempo = self.dummy
        while tempo.next is not None:
            tempo = tempo.next
        tempo.next = Node(val)
       
    def addAtIndex(self, index: int, val: int) -> None: 
        i = -1
        newNode = Node(val)
        tempo = self.dummy
        while tempo.next is not None:
         
            if i == index - 1:
                first = tempo.next
                tempo.next = newNode
                newNode.next = first
                return 
            tempo = tempo.next
            i += 1
        if i == index - 1:
           tempo.next = newNode
        
    def deleteAtIndex(self, index: int) -> None:
        i = -1
        tempo = self.dummy
        while tempo.next is not None:
            
            if i == index - 1:
                tempo.next = tempo.next.next

                return
            i += 1
            tempo = tempo.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)