# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        len_list = 1
        tempo = head
        while tempo.next is not None:
            len_list += 1
            tempo = tempo.next
       
        target = len_list - n + 1
        tempo = dummy
        i = 0
        
        while tempo.next is not None:
            
            if i == (target - 1):
                tempo.next = tempo.next.next
                
                break
            i += 1
            tempo = tempo.next
        return dummy.next
