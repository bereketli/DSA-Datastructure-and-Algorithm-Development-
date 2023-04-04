# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:      
         if head:
            count, tempo  = 1, head
            while tempo.next:
                count += 1
                tempo = tempo.next
        
            target, i = count - (k % count), 1
            tempo = head
            while tempo.next:
                if i == target:
                    shifted = tempo.next
                    tempo.next = None
                    tempo2 = shifted
                    print(shifted)
                    
                    while tempo2.next and tempo2:
                        tempo2 = tempo2.next
                    tempo2.next = head
                    head = shifted
                    break
    
                i += 1
                tempo = tempo.next
            return head
            
            
