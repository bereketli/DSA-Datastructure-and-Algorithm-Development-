# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
           if head is not None:
               self.dummy = ListNode(None)
               self.dummy.next = head
               tempo, index = self.dummy, self.dummy
               while tempo is not None and tempo.next is not None:
                    print("start",self.dummy.next)
                    print("tempo", tempo)
                    if tempo.next.val < x:
                         smaller = tempo.next
                         
                         tempo.next = smaller.next
                         smaller.next = index.next
                         index.next = smaller
                         index = index.next
                         if tempo.next == index:
                            tempo = tempo.next
                         continue

                    tempo = tempo.next
                
                    
              

               return self.dummy.next
