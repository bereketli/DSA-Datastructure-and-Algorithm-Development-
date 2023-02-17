# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            dummy = ListNode(None)
            last_point = dummy
            dummy.next, first_point = head, dummy
            tempo = head
            i = 1 
            while tempo.next is not None:
                if i == (left - 1):
                    first_point = tempo
                if i > left and i <= right:
                    detached = first_point.next
                    first_point.next = tempo
                    tempo = tempo.next
                    first_point.next.next = detached
                else:
                    last_point.next = tempo
                    tempo = tempo.next
                    last_point = last_point.next
                last_point.next = None
                i += 1
           
            if  i > left and i <= right:
                    detached = first_point.next
                    first_point.next = tempo
                    tempo = tempo.next
                    first_point.next.next = detached
            else:
                tempo.next = None
                last_point.next = tempo
            return dummy.next


            



