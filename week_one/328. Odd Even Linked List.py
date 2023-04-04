
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]: 

        if head != None:
            dummy = ListNode(None)
            tempo_even = dummy
            tempo = head
            
            while tempo.next != None and tempo.next.next != None:       
            
                tempo_even.next = tempo.next
                
                tempo.next = tempo.next.next
                tempo = tempo.next
                tempo_even = tempo_even.next
                tempo_even.next = None
                
                
                
            if tempo.next == None:
               
                tempo.next = dummy.next
            else:
                tempo_even.next = tempo.next
                tempo_even = tempo_even.next
                tempo.next = dummy.next
        return head

            

            
            



