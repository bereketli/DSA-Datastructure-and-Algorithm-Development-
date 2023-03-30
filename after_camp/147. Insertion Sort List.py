# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        tempo = head.next
        head.next = None
        maxnode = head
        while tempo :
           
            if tempo.val > maxnode.val:
                maxnode = tempo

            tempo_sorted = dummy
            while tempo_sorted.next and tempo_sorted.next.val < tempo.val:
                tempo_sorted = tempo_sorted.next
            tempo_next = tempo.next
            greater = tempo_sorted.next
            if not tempo_sorted.next:
                tempo.next = None
            tempo_sorted.next = tempo
            tempo.next = greater
            tempo = tempo_next
   
       
        maxnode.next = None
    
        return dummy.next
        
        